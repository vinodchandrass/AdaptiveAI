from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[1]
def load(n):
    with (R/'data'/n).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
a=load('evidence_indicators.csv'); b=load('candidate_status.csv'); c=load('cityspec_contrasts.csv'); d=load('table5_transcriptions.csv')
assert len(a)==263 and len({x['wos_id'] for x in a})==263 and {x['wos_id'] for x in a}=={x['wos_id'] for x in b}
expected={'evaluation':247,'temporal_shift':228,'retention':226,'numerical_table':180,'cost':154,'static_baseline':60,'all_five':29,'control_and_numerical':18}
counts={k:sum(int(x[k]) for x in a) for k in expected};assert counts==expected,(counts,expected)
for x in a:
    assert int(x['all_five'])==int(all(int(x[k]) for k in ['evaluation','temporal_shift','retention','cost','static_baseline']))
    assert int(x['control_and_numerical'])==int(int(x['candidate_control_passages'])>0 and int(x['candidate_table_passages'])>0)
f1={k:round(statistics.mean(float(x['difference_percentage_points']) for x in c if x['domain'].lower()==k and x['metric']=='F1'),2) for k in ['city','topic']};assert f1=={'city':11.29,'topic':18.18},f1
report={'coverage':{k:{'count':v,'percent':round(v/263*100,2)} for k,v in counts.items()},'cityspec_f1':f1,'table5_transcribed_differences':[{**x,'difference':round(float(x['adaptive'])-float(x['baseline']),8)} for x in d],'scope':'Reproduces descriptive arithmetic from existing machine-assisted flags and prior source transcriptions, not original PDF extraction or eligibility.'}
(R/'results'/'extended_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
