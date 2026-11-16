import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

BASE = 'http://127.0.0.1:8000'

def run_tests():
    print("=" * 60)
    print("OMNISCHOLAR GLOBAL AGENTIC UPGRADE & SEO AUDIT")
    print("=" * 60)

    # 1. Test /robots.txt
    print("\n[1/5] Testing GET /robots.txt...")
    req = urllib.request.Request(f'{BASE}/robots.txt')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    ctype = res.headers.get('Content-Type', '')
    assert 'text/plain' in ctype
    robots_text = res.read().decode('utf-8')
    assert 'User-agent: *' in robots_text
    assert 'Disallow: /api/' in robots_text
    assert 'Sitemap: https://scholar.safalai.com.np/sitemap.xml' in robots_text
    print(f"  [PASS] robots.txt verified (length={len(robots_text)}, Content-Type={ctype})")

    # 2. Test /sitemap.xml
    print("\n[2/5] Testing GET /sitemap.xml...")
    req = urllib.request.Request(f'{BASE}/sitemap.xml')
    res = urllib.request.urlopen(req)
    assert res.status == 200
    ctype = res.headers.get('Content-Type', '')
    assert 'xml' in ctype
    sitemap_xml = res.read().decode('utf-8')
    assert 'https://scholar.safalai.com.np/' in sitemap_xml
    assert 'https://scholar.safalai.com.np/#stage1' in sitemap_xml
    # Verify XML validity
    root = ET.fromstring(sitemap_xml)
    urls = [elem.text for elem in root.iter() if elem.tag.endswith('loc')]
    assert len(urls) >= 7
    print(f"  [PASS] sitemap.xml verified ({len(urls)} indexed URLs, Content-Type={ctype})")

    # 3. Test POST /api/agentic-research-council
    print("\n[3/5] Testing POST /api/agentic-research-council...")
    payload = json.dumps({
        'topic': 'Empirical Dynamics of Autonomous Multi-Agent Research Systems',
        'domain': 'Computational Social Science & AI Governance',
        'standard': 'IEEE Transactions'
    }).encode('utf-8')
    req = urllib.request.Request(
        f'{BASE}/api/agentic-research-council',
        data=payload,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    res = urllib.request.urlopen(req)
    assert res.status == 200
    arc_data = json.loads(res.read().decode('utf-8'))
    assert arc_data.get('status') == 'SUCCESS'
    assert 'consensus' in arc_data
    assert 'agents' in arc_data
    agents = arc_data['agents']
    assert 'literature_scout' in agents
    assert 'data_validator' in agents
    assert 'econometrician' in agents
    assert 'editorial_reviewer' in agents
    assert arc_data['consensus']['composite_council_score'] > 0
    assert 'cryptographic_seal' in arc_data
    print(f"  [PASS] Agentic Council executed: Session={arc_data['session_id']}, Score={arc_data['consensus']['composite_council_score']}/100, Verdict={arc_data['consensus']['editorial_verdict']}")

    # 4. Test GET /api/agentic-research-council
    print("\n[4/5] Testing GET /api/agentic-research-council...")
    res = urllib.request.urlopen(f'{BASE}/api/agentic-research-council')
    assert res.status == 200
    arc_get = json.loads(res.read().decode('utf-8'))
    assert arc_get.get('status') == 'SUCCESS'
    print(f"  [PASS] GET /api/agentic-research-council verified: Score={arc_get['consensus']['composite_council_score']}")

    # 5. Test GET /api/market-intelligence
    print("\n[5/5] Testing GET /api/market-intelligence...")
    res = urllib.request.urlopen(f'{BASE}/api/market-intelligence')
    assert res.status == 200
    mi_data = json.loads(res.read().decode('utf-8'))
    assert mi_data.get('status') == 'SUCCESS'
    assert len(mi_data.get('three_billion_dollar_moats', [])) == 3
    assert len(mi_data.get('global_ecosystem_competitors', [])) == 5
    comp_names = [c['name'] for c in mi_data['global_ecosystem_competitors']]
    for expected in ['Consensus', 'Elicit', 'SciSpace (Typeset.io)', 'Paperpal', 'Google NotebookLM']:
        assert any(expected.split()[0] in name for name in comp_names), f"Missing competitor: {expected}"
    assert 'feature_comparison_matrix' in mi_data
    assert 'market_sizing_and_roi' in mi_data
    print(f"  [PASS] Market Intelligence verified: {len(mi_data['three_billion_dollar_moats'])} moats, {len(comp_names)} competitors ({', '.join(comp_names)})")

    print("\n" + "=" * 60)
    print("ALL SPRINT ENDPOINTS 100% OPERATIONAL AND VERIFIED!")
    print("=" * 60)

if __name__ == '__main__':
    run_tests()
