from pathlib import Path
import csv, json, collections, math, re

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    with (ROOT / 'data' / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def key(s):
    return re.sub(r'[^A-Za-z0-9]', '', s).upper()

a = load('corpus_status.csv')
b = load('candidate_status.csv')
c = load('cityspec_contrasts.csv')
g = load('grtp_contrasts.csv')

ids = {key(x['key']) for x in a}
bids = {key(x['wos_id']) for x in b}
assert len(a) == len(ids) == 1379
assert len(b) == len(bids) == 263 and bids <= ids

counts = collections.Counter(x['stage201_screening_outcome'] or 'not_advanced' for x in a)
assert counts == {'Include': 854, 'Uncertain': 121, 'not_advanced': 404}
assert all(x['fulltext_final_status'] == 'NOT_ESTABLISHED' for x in a)
assert all(x['final_eligibility'] == 'NOT_DETERMINED' for x in b)
assert len(c) == 48 and len(g) == 25

for x in c:
    assert math.isclose(
        float(x['adaptive_percent']) - float(x['nonadaptive_percent']),
        float(x['difference_percentage_points']), abs_tol=0.011
    )

for x in g:
    for method in ('GRTP-D', 'GRTP-T'):
        for baseline in ('FT', 'JT', 'FM'):
            assert math.isclose(
                float(x[method]) - float(x[baseline]),
                float(x[f'{method}_minus_{baseline}_rmse_m']), abs_tol=0.011
            )

p, r, cost = (47.68 - 38.97)/10, (43.34 - 27.86)/20, (60 - 37)/30
report = {
    'corpus': len(a),
    'historical_advancement': dict(counts),
    'candidate_count': len(b),
    'candidate_status': dict(collections.Counter(x['final_eligibility'] for x in b)),
    'cityspec_contrasts': len(c),
    'grtp_rows': len(g),
    'illustrative_utility': {
        'weights_0.4_0.4_0.2': .4*p + .4*r - .2*cost,
        'weights_0.2_0.2_0.6': .2*p + .2*r - .6*cost,
        'equal_performance_retention_threshold': ((p+r)/2)/((p+r)/2+cost)
    },
    'scope': 'Arithmetic and identifier checks only; not final eligibility or source authentication.'
}
(ROOT / 'results' / 'verification.json').write_text(
    json.dumps(report, indent=2) + '\n', encoding='utf-8'
)
print(json.dumps(report, indent=2))
