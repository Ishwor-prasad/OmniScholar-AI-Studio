const fs = require("fs");
const path = require("path");

const htmlPath = path.join(__dirname, "..", "app", "static", "index.html");
const jsPath = path.join(__dirname, "..", "app", "static", "app.js");
const cssPath = path.join(__dirname, "..", "app", "static", "style.css");

const html = fs.readFileSync(htmlPath, "utf8");
const js = fs.readFileSync(jsPath, "utf8");
const css = fs.readFileSync(cssPath, "utf8");

// Extract all id="..." from html
const htmlIds = new Set();
const idRegex = /id=["']([^"']+)["']/g;
let m;
while ((m = idRegex.exec(html)) !== null) {
    htmlIds.add(m[1]);
}
console.log(`[FRONTEND AUDIT] Total unique IDs found in index.html: ${htmlIds.size}`);

// Extract getElementById from js
const jsIdRegex = /getElementById\(['"]([^'"]+)['"]\)/g;
const jsIds = new Set();
while ((m = jsIdRegex.exec(js)) !== null) {
    jsIds.add(m[1]);
}
console.log(`[FRONTEND AUDIT] Total unique getElementById targets in app.js: ${jsIds.size}`);

const missingInHtml = [];
for (const id of jsIds) {
    if (!htmlIds.has(id)) {
        missingInHtml.push(id);
    }
}

if (missingInHtml.length > 0) {
    console.error(`[FRONTEND AUDIT ERROR] Missing IDs in index.html:`, missingInHtml);
} else {
    console.log(`[FRONTEND AUDIT SUCCESS] 100% of getElementById calls match elements in index.html!`);
}

// Extract querySelector with #id from js
const qsRegex = /querySelector\(['"]#([^'"]+)['"]\)/g;
const qsIds = new Set();
while ((m = qsRegex.exec(js)) !== null) {
    qsIds.add(m[1]);
}
const missingQs = [];
for (const id of qsIds) {
    if (!htmlIds.has(id)) {
        missingQs.push(id);
    }
}
if (missingQs.length > 0) {
    console.error(`[FRONTEND AUDIT ERROR] Missing querySelector IDs in index.html:`, missingQs);
} else {
    console.log(`[FRONTEND AUDIT SUCCESS] 100% of querySelector(#id) targets match elements in index.html!`);
}

// Extract endpoints
const fetchRegex = /fetch\(['"]([^'"]+)['"]/g;
const endpoints = new Set();
while ((m = fetchRegex.exec(js)) !== null) {
    endpoints.add(m[1]);
}
console.log(`[FRONTEND AUDIT] Endpoints called in app.js:`, Array.from(endpoints));

// Check CSS unclosed braces or basic integrity
let openBraces = (css.match(/\{/g) || []).length;
let closeBraces = (css.match(/\}/g) || []).length;
console.log(`[CSS AUDIT] Open braces: ${openBraces}, Close braces: ${closeBraces}`);
if (openBraces === closeBraces) {
    console.log(`[CSS AUDIT SUCCESS] CSS brace parity verified!`);
} else {
    console.error(`[CSS AUDIT ERROR] CSS brace mismatch! Open: ${openBraces}, Close: ${closeBraces}`);
}

