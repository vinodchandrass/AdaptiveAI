from pathlib import Path
import json,csv
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; out=R/'results'; report=json.loads((out/'extended_verification.json').read_text()); coverage=report['coverage']; labels=[k.replace('_',' ').capitalize() for k in coverage]; vals=[v['percent'] for v in coverage.values()]; fig,ax=plt.subplots(figsize=(7.1,4)); ax.barh(labels,vals); ax.invert_yaxis();ax.set_xlim(0,110);ax.set_xlabel('Candidate documents (%)');ax.bar_label(ax.containers[0],fmt='%.2f%%',padding=3);fig.tight_layout();fig.savefig(out/'Figure3_reproduced.png',dpi=600);plt.close(fig)
rows=[x for x in report['table5_transcribed_differences'] if x['study']=='SD'];fig,axes=plt.subplots(1,3,figsize=(7.1,2.8));
for ax,row in zip(axes,rows):
 ax.bar(['Replay','Replay + SD'],[float(row['baseline']),float(row['adaptive'])]);ax.set_title(row['metric']);ax.set_ylabel(row['unit']);ax.tick_params(axis='x',rotation=20);ax.bar_label(ax.containers[0],fmt='%.2f',padding=2);ax.set_ylim(0,max(float(row['baseline']),float(row['adaptive']))*1.2)
fig.tight_layout();fig.savefig(out/'Figure4_reproduced.png',dpi=600);plt.close(fig)
