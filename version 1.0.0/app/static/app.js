// Project OmniScholar - Research AI Studio v1.0.0 Frontend Logic

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const btnLoadSample = document.getElementById('btnLoadSample');
    const btnExportPdf = document.getElementById('btnExportPdf');
    const btnExportZip = document.getElementById('btnExportZip');
    const btnExportTex = document.getElementById('btnExportTex');
    const btnManuscriptPdf = document.getElementById('btnManuscriptPdf');
    const datasetMeta = document.getElementById('datasetMeta');
    
    // Meta fields
    const metaFilename = document.getElementById('metaFilename');
    const metaSampleSize = document.getElementById('metaSampleSize');
    const metaVarCount = document.getElementById('metaVarCount');
    const metaHash = document.getElementById('metaHash');
    const selectGroupCol = document.getElementById('selectGroupCol');
    const activeGroupBadge = document.getElementById('activeGroupBadge');

    // Tab buttons & panes
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    // Content containers
    const variablesGrid = document.getElementById('variablesGrid');
    const inferentialContainer = document.getElementById('inferentialContainer');
    const heatmapBox = document.getElementById('heatmapBox');
    const latexContainer = document.getElementById('latexContainer');
    const manuscriptText = document.getElementById('manuscriptText');
    const btnCopyManuscript = document.getElementById('btnCopyManuscript');
    const wordCount = document.getElementById('wordCount');
    const charCount = document.getElementById('charCount');
    const passportBox = document.getElementById('passportBox');

    // Modal elements
    const imageModal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const closeModal = document.getElementById('closeModal');

    // 1. Tab Navigation
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const targetId = btn.getAttribute('data-tab');
            const targetPane = document.getElementById(targetId);
            if (targetPane) {
                targetPane.classList.add('active');
            }
        });
    });

    // 2. Upload & Sample Handlers
    dropzone.addEventListener('click', () => fileInput.click());

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'var(--primary)';
    });

    dropzone.addEventListener('dragleave', () => {
        dropzone.style.borderColor = 'rgba(255, 255, 255, 0.15)';
    });

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.style.borderColor = 'rgba(255, 255, 255, 0.15)';
        if (e.dataTransfer.files.length > 0) {
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            handleFileUpload(fileInput.files[0]);
        }
    });

    btnLoadSample.addEventListener('click', async () => {
        btnLoadSample.disabled = true;
        btnLoadSample.innerHTML = '⚡ Processing Empirical Pipeline...';
        try {
            const resp = await fetch('/api/load-sample', { method: 'POST' });
            if (!resp.ok) throw new Error('Failed to load sample dataset');
            const data = await resp.json();
            renderDashboard(data);
        } catch (err) {
            alert('Error loading sample dataset: ' + err.message);
        } finally {
            btnLoadSample.disabled = false;
            btnLoadSample.innerHTML = '⚡ Load Sample Research Dataset';
        }
    });

    async function handleFileUpload(file) {
        const formData = new FormData();
        formData.append('file', file);

        const originalText = dropzone.querySelector('h3').textContent;
        dropzone.querySelector('h3').textContent = 'Uploading, auditing and compiling PDF...';

        try {
            const resp = await fetch('/api/upload', {
                method: 'POST',
                body: formData
            });
            if (!resp.ok) {
                const errData = await resp.json().catch(() => ({}));
                throw new Error(errData.detail || 'Upload analysis failed');
            }
            const data = await resp.json();
            renderDashboard(data);
        } catch (err) {
            alert('Error processing uploaded file: ' + err.message);
        } finally {
            dropzone.querySelector('h3').textContent = originalText;
        }
    }

    // 3. Grouping Selector Change Handler
    selectGroupCol.addEventListener('change', async () => {
        const chosenCol = selectGroupCol.value;
        if (!chosenCol) return;

        try {
            selectGroupCol.disabled = true;
            const resp = await fetch('/api/set-grouping', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ group_col: chosenCol })
            });
            if (!resp.ok) throw new Error('Failed to update grouping cohort');
            const data = await resp.json();
            renderDashboard(data);
        } catch (err) {
            alert('Error updating grouping: ' + err.message);
        } finally {
            selectGroupCol.disabled = false;
        }
    });

    // 4. Render Dashboard with Verified Data
    function renderDashboard(data) {
        const summary = data.summary;

        // Populate metadata strip
        datasetMeta.style.display = 'flex';
        metaFilename.textContent = data.filename;
        metaSampleSize.textContent = summary.sample_size;
        metaVarCount.textContent = summary.total_variables;
        metaHash.textContent = summary.data_hash_sha256.substring(0, 16) + '...';

        // Populate Grouping Selector
        selectGroupCol.innerHTML = '';
        if (data.available_grouping_cols && data.available_grouping_cols.length > 0) {
            data.available_grouping_cols.forEach(col => {
                const opt = document.createElement('option');
                opt.value = col;
                opt.textContent = col.length > 30 ? col.substring(0, 30) + '...' : col;
                if (col === data.active_group_col) {
                    opt.selected = true;
                }
                selectGroupCol.appendChild(opt);
            });
            selectGroupCol.style.display = 'inline-block';
            activeGroupBadge.textContent = data.active_group_col || 'None';
        } else {
            selectGroupCol.style.display = 'none';
            activeGroupBadge.textContent = 'None Available';
        }

        // 4.1 Tab 1: Variables
        variablesGrid.innerHTML = '';
        Object.entries(summary.variables).forEach(([colName, vInfo]) => {
            const card = document.createElement('div');
            card.className = 'variable-card';

            let statsHtml = `<span>N: <strong>${vInfo.count}</strong></span>`;
            if (vInfo.type === 'numeric') {
                statsHtml += `<span>Mean: <strong>${vInfo.mean}</strong></span><span>SD: <strong>${vInfo.std}</strong></span>`;
            } else {
                statsHtml += `<span>Missing: <strong>${vInfo.missing}</strong> (${vInfo.missing_pct}%)</span>`;
            }

            let freqRows = '';
            vInfo.frequencies.slice(0, 4).forEach(f => {
                freqRows += `<tr><td>${f.category}</td><td>${f.count}</td><td><strong>${f.percentage}%</strong></td></tr>`;
            });

            card.innerHTML = `
                <div class="var-header">
                    <h3 class="var-title">${colName}</h3>
                    <span class="var-type-badge">${vInfo.type}</span>
                </div>
                <div class="var-stats-row">${statsHtml}</div>
                <table class="var-freq-table">
                    <thead><tr><th>Category</th><th>Count</th><th>Pct</th></tr></thead>
                    <tbody>${freqRows}</tbody>
                </table>
                <div class="var-chart-preview" data-src="${vInfo.chart_url}">
                    <img src="${vInfo.chart_url}" alt="Figure for ${colName}" loading="lazy">
                </div>
            `;
            variablesGrid.appendChild(card);
        });

        // Attach modal click on charts
        document.querySelectorAll('.var-chart-preview').forEach(div => {
            div.addEventListener('click', () => {
                const src = div.getAttribute('data-src');
                modalImg.src = src;
                imageModal.style.display = 'flex';
            });
        });

        // 4.2 Tab 2: Inferential & Correlation
        inferentialContainer.innerHTML = '';
        if (summary.inferential && summary.inferential.length > 0) {
            summary.inferential.forEach(inf => {
                const card = document.createElement('div');
                card.className = 'inferential-card';
                card.innerHTML = `
                    <div class="inferential-header">
                        <h4>${inf.test}</h4>
                        <span class="sig-badge ${inf.significant ? 'pass' : 'null'}">
                            ${inf.significant ? 'Statistically Significant (p < .05)' : 'Fail to Reject Null (p > .05)'}
                        </span>
                    </div>
                    <p style="font-size:0.85rem; margin-bottom: 0.5rem;">Target: <strong>${inf.target_variable}</strong> across <strong>${inf.grouping_variable}</strong></p>
                    <div style="font-family: var(--font-mono); font-size:0.8rem; background: rgba(0,0,0,0.3); padding:0.5rem; border-radius:4px; margin-bottom:0.5rem;">
                        Test Statistic: ${inf.statistic} | Degrees of Freedom (df): ${inf.df} | p-value: ${inf.p_value}
                    </div>
                    <p style="font-size:0.85rem; color: var(--text-secondary);">${inf.interpretation}</p>
                `;
                inferentialContainer.appendChild(card);
            });
        } else {
            inferentialContainer.innerHTML = '<p class="placeholder-text">No inferential groupings identified or sample size too small.</p>';
        }

        if (summary.correlation && summary.correlation.chart_url) {
            heatmapBox.innerHTML = `
                <img src="${summary.correlation.chart_url}" alt="Correlation Heatmap" style="cursor:pointer;" id="heatmapImg">
            `;
            document.getElementById('heatmapImg').addEventListener('click', () => {
                modalImg.src = summary.correlation.chart_url;
                imageModal.style.display = 'flex';
            });
        }

        // 4.3 Tab 3: LaTeX Booktabs
        latexContainer.innerHTML = '';
        if (summary.latex_tables && summary.latex_tables.length > 0) {
            summary.latex_tables.forEach((t, idx) => {
                const card = document.createElement('div');
                card.className = 'latex-card';
                card.innerHTML = `
                    <div class="latex-card-header">
                        <h4>Table ${idx + 1}: ${t.variable}</h4>
                        <button class="btn btn-sm btn-secondary copy-latex-btn" data-code="${encodeURIComponent(t.latex)}">
                            📋 Copy LaTeX
                        </button>
                    </div>
                    <pre class="latex-code-block">${t.latex}</pre>
                `;
                latexContainer.appendChild(card);
            });

            document.querySelectorAll('.copy-latex-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const code = decodeURIComponent(btn.getAttribute('data-code'));
                    navigator.clipboard.writeText(code);
                    btn.textContent = '✅ Copied!';
                    setTimeout(() => btn.textContent = '📋 Copy LaTeX', 2000);
                });
            });
        }

        // 4.4 Tab 4: Manuscript Draft & Text Stats
        manuscriptText.value = summary.draft_text;
        updateManuscriptStats(summary.draft_text);

        // 4.5 Tab 5: Passport
        const pass = summary.passport;
        passportBox.innerHTML = `
            <div class="passport-seal">
                <div class="seal-icon">🛡️</div>
                <div class="seal-title">
                    <h3>Cryptographic Reproducibility Passport</h3>
                    <p style="font-size:0.85rem; color: var(--text-secondary);">${pass.audit_statement}</p>
                </div>
            </div>
            <div class="passport-grid">
                <div class="pass-row">
                    <span class="pass-label">Audit Status:</span>
                    <span class="pass-value" style="color: var(--success);">${pass.status}</span>
                </div>
                <div class="pass-row">
                    <span class="pass-label">Ghostwriting Risk Index:</span>
                    <span class="pass-value" style="color: var(--success);">${pass.ghostwriting_risk_score}</span>
                </div>
                <div class="pass-row">
                    <span class="pass-label">Verified Sample Size:</span>
                    <span class="pass-value">N = ${pass.sample_size}</span>
                </div>
                <div class="pass-row">
                    <span class="pass-label">Execution Environment:</span>
                    <span class="pass-value">${pass.code_sandbox}</span>
                </div>
                <div class="pass-row" style="grid-column: 1 / -1;">
                    <span class="pass-label">Dataset SHA-256 Fingerprint:</span>
                    <span class="pass-value mono">${pass.sha256_checksum}</span>
                </div>
                <div class="pass-row" style="grid-column: 1 / -1;">
                    <span class="pass-label">Audit Timestamp (UTC):</span>
                    <span class="pass-value mono">${pass.timestamp_utc}</span>
                </div>
            </div>
            <div style="display:flex; justify-content:center; gap:1rem; margin-top: 1.5rem; flex-wrap:wrap;">
                <button class="btn btn-primary" id="btnPassportPdf">
                    📄 Download Compiled Manuscript (PDF)
                </button>
                <button class="btn btn-secondary" id="btnPassportDownload">
                    📥 Download Full Package (.ZIP)
                </button>
            </div>
        `;
        document.getElementById('btnPassportDownload').addEventListener('click', downloadZip);
        document.getElementById('btnPassportPdf').addEventListener('click', downloadPdf);
    }

    // 5. Manuscript Stats Updater
    function updateManuscriptStats(text) {
        if (!text) {
            wordCount.textContent = '0';
            charCount.textContent = '0';
            return;
        }
        const words = text.trim().split(/\s+/).filter(Boolean).length;
        wordCount.textContent = words.toLocaleString();
        charCount.textContent = text.length.toLocaleString();
    }

    manuscriptText.addEventListener('input', () => {
        updateManuscriptStats(manuscriptText.value);
    });

    // 6. Copy Manuscript Draft
    btnCopyManuscript.addEventListener('click', () => {
        navigator.clipboard.writeText(manuscriptText.value);
        btnCopyManuscript.textContent = '✅ Copied Draft!';
        setTimeout(() => btnCopyManuscript.textContent = '📋 Copy Markdown Text', 2000);
    });

    // 7. Download Handlers
    function downloadZip() {
        window.location.href = '/api/export-zip';
    }
    function downloadPdf() {
        window.location.href = '/api/export-pdf';
    }
    function downloadTex() {
        window.location.href = '/api/export-tex';
    }

    btnExportZip.addEventListener('click', downloadZip);
    btnExportPdf.addEventListener('click', downloadPdf);
    btnManuscriptPdf.addEventListener('click', downloadPdf);
    btnExportTex.addEventListener('click', downloadTex);

    // 8. Modal Controls
    closeModal.addEventListener('click', () => {
        imageModal.style.display = 'none';
    });
    window.addEventListener('click', (e) => {
        if (e.target === imageModal) {
            imageModal.style.display = 'none';
        }
    });
});
