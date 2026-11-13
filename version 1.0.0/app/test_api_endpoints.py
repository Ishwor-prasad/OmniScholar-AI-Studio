import urllib.request
import urllib.parse
import json
import os
import sys

BASE = 'http://127.0.0.1:8000'

def test_api():
    print("=" * 60)
    print("OMNISCHOLAR v1.0.0 - BACKEND SUITE COMPREHENSIVE VERIFICATION")
    print("=" * 60)

    # 1. Synthesize topic
    print("1. Testing /api/synthesize-topic...")
    payload = json.dumps({
        'topic': 'The Impact of Algorithmic Transparency on Institutional Trust and Market Volatility',
        'domain': 'Finance & FinTech',
        'standard': 'IEEE'
    }).encode()
    req = urllib.request.Request(f'{BASE}/api/synthesize-topic', data=payload, headers={'Content-Type': 'application/json'}, method='POST')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    data = json.loads(res.read().decode())
    assert data.get('topic') or data.get('topic_raw')
    assert 'theoretical_model' in data
    assert len(data.get('hypotheses', [])) >= 3
    print(f"  [PASS] Synthesized title: {data.get('declarative_title')}")
    print(f"  [PASS] Hypotheses generated: {len(data.get('hypotheses'))}")

    # 2. Generate survey data
    print("\n2. Testing /api/generate-survey-data...")
    s_payload = json.dumps({'topic': 'Impact of Algorithmic Transparency', 'domain': 'Finance', 'sample_size': 100}).encode()
    req = urllib.request.Request(f'{BASE}/api/generate-survey-data', data=s_payload, headers={'Content-Type': 'application/json'}, method='POST')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    s_data = json.loads(res.read().decode())
    assert s_data['status'] == 'success'
    assert s_data['sample_size'] == 100
    assert len(s_data['columns']) >= 8
    print(f"  [PASS] Generated records: {s_data['sample_size']} across {len(s_data['columns'])} columns")

    # 3. Run Autonomous Pipeline
    print("\n3. Testing /api/run-autonomous-pipeline...")
    p_payload = json.dumps({
        'topic': 'The Impact of Algorithmic Transparency on Institutional Trust and Market Volatility',
        'domain': 'Finance',
        'standard': 'IEEE',
        'sample_size': 100
    }).encode()
    req = urllib.request.Request(f'{BASE}/api/run-autonomous-pipeline', data=p_payload, headers={'Content-Type': 'application/json'}, method='POST')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    p_data = json.loads(res.read().decode())
    assert p_data['status'] == 'success'
    assert p_data['stage'] == 'completed'
    assert p_data['sample_size'] == 100
    assert 'summary' in p_data
    summary = p_data['summary']
    assert summary.get('typst_generated') or summary.get('pdf_generated')
    print(f"  [PASS] Pipeline completed: sample={summary['sample_size']}, run_id={summary.get('run_id')}")
    print(f"  [PASS] Typst compiled: {summary.get('typst_generated')}, PDF generated: {summary.get('pdf_generated')}")

    # 4. Preview PDF (HEAD and GET)
    print("\n4. Testing /api/preview-pdf...")
    req = urllib.request.Request(f'{BASE}/api/preview-pdf', method='HEAD')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    assert res.headers.get('Content-Type') == 'application/pdf'
    assert 'inline' in res.headers.get('Content-Disposition', '')
    print(f"  [PASS] HEAD /api/preview-pdf: status=200, Content-Type={res.headers.get('Content-Type')}, Content-Disposition={res.headers.get('Content-Disposition')}")

    req = urllib.request.Request(f'{BASE}/api/preview-pdf', method='GET')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    pdf_bytes = res.read()
    assert pdf_bytes.startswith(b'%PDF')
    print(f"  [PASS] GET /api/preview-pdf: received {len(pdf_bytes):,} bytes valid PDF binary")

    # 5. Peer review endpoint
    print("\n5. Testing /api/peer-review...")
    res = urllib.request.urlopen(f'{BASE}/api/peer-review')
    assert res.status == 200
    pr_data = json.loads(res.read().decode())
    assert 'editorial_decision' in pr_data
    assert len(pr_data.get('reviewers', [])) == 3
    print(f"  [PASS] Decision: {pr_data['editorial_decision']}, Composite Score: {pr_data['composite_quality_score']}/100, Reviewers: {len(pr_data['reviewers'])}")

    # 6. Ledger endpoint
    print("\n6. Testing /api/ledger...")
    res = urllib.request.urlopen(f'{BASE}/api/ledger')
    assert res.status == 200
    l_data = json.loads(res.read().decode())
    assert 'ledger' in l_data
    assert len(l_data['ledger']) > 0
    print(f"  [PASS] Ledger records: {l_data['total_records']}, Dataset SHA-256: {l_data['dataset_sha256'][:16]}...")

    # 7. Export Typst
    print("\n7. Testing /api/export-typst...")
    res = urllib.request.urlopen(f'{BASE}/api/export-typst?compile=false')
    assert res.status == 200
    typ_content = res.read().decode('utf-8', errors='ignore')
    assert '#import' in typ_content or '#set' in typ_content or 'Safal AI' in typ_content
    print(f"  [PASS] Typst source exported ({len(typ_content):,} chars)")

    # 8. Export Zip
    print("\n8. Testing /api/export-zip...")
    res = urllib.request.urlopen(f'{BASE}/api/export-zip')
    assert res.status == 200
    zip_bytes = res.read()
    assert zip_bytes.startswith(b'PK')
    print(f"  [PASS] Export ZIP generated: {len(zip_bytes):,} bytes archive")

    print("\n" + "=" * 60)
    print("SUCCESS: ALL 8 ENDPOINTS FULLY VERIFIED AND AUDIT-READY!")
    print("=" * 60)

if __name__ == '__main__':
    test_api()
