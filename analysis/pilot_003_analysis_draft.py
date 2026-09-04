"""PILOT_003 FREEZE-CANDIDATE deterministic analysis. NOT FROZEN."""
from __future__ import annotations
import json,random
from pathlib import Path
from statistics import mean,median
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'trajectories/raw'
PRIMARY=('SAME+REFL','SAME-REFL','OTHER+REFL','OTHER-REFL'); LABEL=('LABEL_OWN+REFL','LABEL_OWN-REFL','LABEL_OTHER+REFL','LABEL_OTHER-REFL'); CAL={f'P003-{i:03d}' for i in range(1,9)}
def m(r,a,f='related'):return r['primary'][a][f]['m']
def delta(r,f='related'):
 v=[m(r,a,f) for a in PRIMARY];return None if any(x is None for x in v) else (v[0]-v[1])-(v[2]-v[3])
def dlabel(r):
 v=[r['label_controls'][a]['m'] for a in LABEL];return None if any(x is None for x in v) else (v[0]-v[1])-(v[2]-v[3])
def dnull(r):
 a=r['placebo']['NULLREL+REFL']['m'];b=r['placebo']['NULLREL-REFL']['m'];return None if a is None or b is None else a-b
def boot(xs,seed,n=10000):
 xs=[x for x in xs if x is not None]
 if not xs:return [None,None]
 q=random.Random(seed);z=sorted(mean(q.choice(xs) for _ in xs) for _ in range(n));return [z[int(.025*n)],z[min(n-1,int(.975*n))]]
def vec(pairs,seed):
 pairs=[p for p in pairs if p[1] is not None];xs=[p[1] for p in pairs]
 return {'n':len(xs),'mean':mean(xs) if xs else None,'median':median(xs) if xs else None,'bootstrap_95_ci':boot(xs,seed),'by_seed':[{'seed_id':s,'value':v} for s,v in pairs]}
def first_attempts(records):
 by={}
 for r in sorted(records,key=lambda x:(x['seed_id'],x.get('attempt',1))):by.setdefault(r['seed_id'],r)
 return list(by.values())
def calibration(rs):
 flips=[];details=[]
 for r in rs:
  if r['seed_id'] not in CAL or r.get('excluded'):continue
  for a in PRIMARY:
   x=m(r,a);y=r.get('calibration',{}).get(a,{}).get('m')
   if x is not None and y is not None:flips.append(abs(x-y));details.append({'seed_id':r['seed_id'],'arm':a,'primary':x,'repeat':y,'flip':abs(x-y)})
 if not flips:return {'n_pairs':0,'agreement_rate':None,'flip_rate':None,'epsilon_related':None,'details':[]}
 sf=sorted(flips);return {'n_pairs':len(flips),'agreement_rate':mean(1-x for x in flips),'flip_rate':mean(flips),'epsilon_related':sf[min(len(sf)-1,int(.95*len(sf)))],'details':details}
def conflict(rs):
 details=[];disc=0;tool=claim=missing=0
 for r in rs:
  if r.get('excluded'):continue
  s=m(r,'SAME+REFL');o=m(r,'OTHER+REFL')
  if s is None or o is None or s==o:continue
  disc+=1;row={'seed_id':r['seed_id'],'arms':[]}
  for name,t,c in [('CLAIM_OWN_TOOL_OTHER',o,s),('CLAIM_OTHER_TOOL_SAME',s,o)]:
   x=r.get('conflict',{}).get(name,{}).get('m');tm=None if x is None else x==t;cm=None if x is None else x==c
   if x is None:missing+=1
   else:tool+=int(tm);claim+=int(cm)
   row['arms'].append({'arm':name,'m':x,'tool_match':tm,'claim_match':cm})
  details.append(row)
 return {'discriminating_seeds':disc,'evaluated_arms':2*disc-missing,'missing_arms':missing,'tool_matches':tool,'claim_matches':claim,'details':details}
def cells(rs,f='related'):
 out={}
 for a in PRIMARY:
  vals=[m(r,a,f) for r in rs if not r.get('excluded') and m(r,a,f) is not None];out[a]={'n':len(vals),'mean_B_rate':mean(vals) if vals else None}
 return out
def integrity(allr):
 calls=[x for r in allr for x in r.get('tool_integrity',[])];fields=('tool_requested','tool_call_parsed','bundle_id_match','tool_result_delivered','registry_match','answer_after_tool')
 return {'n_logged_calls':len(calls),'all_required_true':all(all(x.get(k) is True for k in fields) for x in calls) if calls else False,'failures':[{'seed_id':r['seed_id'],'attempt':r.get('attempt'),'arm':x.get('arm'),'failed':[k for k in fields if x.get(k) is not True]} for r in allr for x in r.get('tool_integrity',[]) if any(x.get(k) is not True for k in fields)]}
def summarize(allr):
 rs=first_attempts(allr);inc=[r for r in rs if not r.get('excluded')]
 return {'pilot':'PILOT_003','status':'FREEZE_CANDIDATE_ANALYSIS','n_attempt_records':len(allr),'n_seed_first_attempts':len(rs),'n_included_first_attempts':len(inc),'excluded':[{'seed_id':r['seed_id'],'attempt':r.get('attempt'),'code':r.get('exclusion_code')} for r in rs if r.get('excluded')],'primary_cell_means_related':cells(inc,'related'),'primary_cell_means_unrelated':cells(inc,'unrelated'),'delta_I1SIM_related':vec([(r['seed_id'],delta(r,'related')) for r in inc],3001),'delta_I1SIM_unrelated':vec([(r['seed_id'],delta(r,'unrelated')) for r in inc],3002),'T_I1SIM':vec([(r['seed_id'],None if delta(r,'related') is None or delta(r,'unrelated') is None else delta(r,'related')-delta(r,'unrelated')) for r in inc],3003),'delta_I0_label_related':vec([(r['seed_id'],dlabel(r)) for r in inc],3004),'delta_NULL_related':vec([(r['seed_id'],dnull(r)) for r in inc],3005),'calibration':calibration(rs),'conflict_diagnostic':conflict(rs),'tool_integrity_all_attempts':integrity(allr)}
def load():return [json.loads(p.read_text()) for p in sorted(RAW.glob('P003-*.attempt-*.json'))]
if __name__=='__main__':
 r=load()
 if not r:raise SystemExit('No P003 attempt records. Do not run target data before freeze.')
 print(json.dumps(summarize(r),indent=2))
