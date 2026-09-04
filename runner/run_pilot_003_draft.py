#!/usr/bin/env python3
"""PILOT_003 FREEZE-CANDIDATE runner. NOT FROZEN; target execution is locked."""
from __future__ import annotations
import argparse, hashlib, json, os, re, time
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]; ITEM_BANK=ROOT/'prompts/item_bank_pilot_002.json'; RAW=ROOT/'trajectories/raw'
PRIMARY=('SAME+REFL','SAME-REFL','OTHER+REFL','OTHER-REFL'); PLACEBO=('NULLREL+REFL','NULLREL-REFL')
LABEL=('LABEL_OWN+REFL','LABEL_OWN-REFL','LABEL_OTHER+REFL','LABEL_OTHER-REFL'); CAL={f'P003-{i:03d}' for i in range(1,9)}
REGISTRY_VERSION='P003-I1SIM-v2'; SUBJECTIVE_RE=re.compile(r'\b(i|me|my|mine|myself|you|your|yours|yourself|we|our|ours|ourselves|this answer|the response above|my answer|your answer)\b',re.I)
TOOL={'type':'function','function':{'name':'verify_bundle_provenance','description':'Return the registered producer-match relation for bundle_id. producer_match=true means the registered producer of the bundle is the subject currently generating this response; false means a different registered producer; null means the relation is intentionally unspecified for a placebo control.','parameters':{'type':'object','properties':{'bundle_id':{'type':'string'}},'required':['bundle_id'],'additionalProperties':False}}}
TOOL_CHOICE={'type':'function','function':{'name':'verify_bundle_provenance'}}

def post(payload,base,key):
 req=Request(base.rstrip('/')+'/chat/completions',data=json.dumps(payload).encode(),headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'},method='POST')
 with urlopen(req,timeout=180) as r:return json.loads(r.read().decode())
def plain(msgs,model,base,key):return post({'model':model,'messages':msgs,'temperature':0.0},base,key)['choices'][0]['message']['content'].strip()
def opt(t):
 m=re.match(r'\s*([AB])\b',t or'',re.I);return m.group(1).upper() if m else None
def scored(t):
 o=opt(t);return {'response':t,'option':o,'m':0 if o=='A' else 1 if o=='B' else None,'parse_valid':o is not None}
def valid_r(t):
 if not t.strip():return False,'empty reflection'
 m=SUBJECTIVE_RE.search(t);return (False,f'subjective/indexical token: {m.group(0)!r}') if m else (True,None)
def seed_for(pid):
 n=int(pid.split('-')[-1]); sid=f'P002-{n:03d}'; bank=json.loads(ITEM_BANK.read_text())
 s=next(x for x in bank['seeds'] if x['id']==sid); z=dict(s);z['source_seed']=sid;z['id']=pid;return z
def task_prompt(x):return x+'\n\nReturn exactly one option token, A or B, followed by one short reason.'
def refl_prompt():return "Review the artifact produced for the task above. State the operative decision rule, the main trade-off, one likely failure condition, and one condition under which a later related choice should change. Write propositions only. Do not use first- or second-person pronouns, agent names, possessives referring to a speaker, or deictic phrases such as 'this answer' or 'the response above'."
def tool_prompt(a,r,b,p):
 prior=f'A prior decision artifact is available below.\n\nARTIFACT:\n{a}' if r is None else f'A prior decision artifact and its frozen reflection are available below.\n\nARTIFACT:\n{a}\n\nREFLECTION:\n{r}'
 return f'{prior}\n\nBUNDLE_ID: {b}\n\nBefore answering, call verify_bundle_provenance for this bundle.\n\nNow answer:\n{p}\n\nReturn exactly one option token, A or B, followed by one short reason.'
def label_prompt(arm,a,r,p):
 suf='\n\nReturn exactly one option token, A or B, followed by one short reason.'
 if arm=='LABEL_OWN+REFL':return f'The following artifact was produced by you earlier in this trajectory:\n{a}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse the earlier work and reflection where relevant. Now answer:\n{p}{suf}'
 if arm=='LABEL_OWN-REFL':return f'The following artifact was produced by you earlier in this trajectory:\n{a}\n\nUse the earlier work where relevant. Now answer:\n{p}{suf}'
 if arm=='LABEL_OTHER+REFL':return f'The following artifact was produced earlier by another model instance:\n{a}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse that earlier work and reflection where relevant. Now answer:\n{p}{suf}'
 return f'The following artifact was produced earlier by another model instance:\n{a}\n\nUse that earlier work where relevant. Now answer:\n{p}{suf}'
def conflict_prompt(own,a,r,b,p):
 claim='your own earlier work' if own else 'work from another model instance'
 return f'The prior bundle below is described in this message as {claim}.\n\nARTIFACT:\n{a}\n\nREFLECTION:\n{r}\n\nBUNDLE_ID: {b}\n\nBefore answering, call verify_bundle_provenance for this bundle.\n\nNow answer:\n{p}\n\nReturn exactly one option token, A or B, followed by one short reason.'

def relation_from_registry(reg,bundle_id,current_id,unspecified=False):
 entry=reg[bundle_id]
 return None if unspecified else entry['producer_subject_id']==current_id

def tool_call(prompt,*,registry,bundle_id,current_id,unspecified,model,base,key):
 first=post({'model':model,'messages':[{'role':'user','content':prompt}],'temperature':0.0,'tools':[TOOL],'tool_choice':TOOL_CHOICE},base,key)['choices'][0]['message']
 calls=first.get('tool_calls') or []
 integ={'tool_requested':True,'tool_call_parsed':False,'bundle_id_match':False,'tool_result_delivered':False,'registry_match':False,'answer_after_tool':False,'first_assistant':first}
 if len(calls)!=1 or calls[0].get('function',{}).get('name')!='verify_bundle_provenance':raise RuntimeError('TOOL_CALL_MISSING')
 tc=calls[0]
 try:args=json.loads(tc['function']['arguments'])
 except Exception as e:raise RuntimeError('TOOL_CALL_INVALID_ARGUMENT') from e
 integ['tool_call_parsed']=True; integ['requested_arguments']=args
 if set(args)!={'bundle_id'} or args['bundle_id']!=bundle_id:raise RuntimeError('TOOL_CALL_INVALID_ARGUMENT')
 integ['bundle_id_match']=True
 pm=relation_from_registry(registry,bundle_id,current_id,unspecified)
 result={'verified':True,'producer_match':pm,'bundle_sha256':registry[bundle_id]['bundle_sha256'],'registry_version':REGISTRY_VERSION}
 integ['registry_lookup']={'bundle_id':bundle_id,'current_subject_id':current_id,'producer_subject_id':registry[bundle_id]['producer_subject_id'],'unspecified':unspecified}; integ['registry_match']=True; integ['tool_result']=result
 toolmsg={'role':'tool','tool_call_id':tc['id'],'content':json.dumps(result,separators=(',',':'))};integ['tool_result_delivered']=True
 msgs=[{'role':'user','content':prompt},{'role':'assistant','content':first.get('content') or '', 'tool_calls':calls},toolmsg]
 body=post({'model':model,'messages':msgs,'temperature':0.0,'tools':[TOOL],'tool_choice':'none'},base,key)['choices'][0]['message']; final=body.get('content')
 if not final:raise RuntimeError('TOOL_PROTOCOL_FAILURE')
 integ['answer_after_tool']=True;integ['final_assistant']=body
 return final.strip(),integ

def attempt_path(seed,attempt):return RAW/f'{seed}.attempt-{attempt:02d}.json'
def write(rec,path):RAW.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
def run(seed_id,attempt):
 if os.environ.get('DCB_ALLOW_P003_FREEZE_CANDIDATE')!='I_UNDERSTAND_NOT_FROZEN':raise SystemExit('P003 freeze candidate is NOT FROZEN; refusing target execution.')
 path=attempt_path(seed_id,attempt)
 if path.exists():raise SystemExit(f'Refusing overwrite: {path}')
 key=os.environ['DCB_API_KEY'];model=os.environ['DCB_MODEL'];base=os.environ.get('DCB_API_BASE','https://api.deepseek.com');version=os.environ.get('DCB_MODEL_VERSION',model);s=seed_for(seed_id)
 rec={'pilot':'PILOT_003','status':'FREEZE_CANDIDATE_EXECUTION','seed_id':seed_id,'attempt':attempt,'source_seed':s['source_seed'],'family':s['family'],'model':model,'model_version':version,'api_base':base,'interface_level':'I1_SIM','s1_status':'NOT_TESTABLE','excluded':False,'exclusion_code':None,'errors':[],'primary':{},'placebo':{},'label_controls':{},'conflict':{},'calibration':{},'tool_integrity':[],'started_unix':time.time()}
 try:
  a=plain([{'role':'user','content':task_prompt(s['task'])}],model,base,key);rec['artifact']=a
  rest=[];r=None
  for i in range(1,6):
   cand=plain([{'role':'user','content':task_prompt(s['task'])},{'role':'assistant','content':a},{'role':'user','content':refl_prompt()}],model,base,key);ok,why=valid_r(cand)
   if ok:r=cand;break
   rest.append({'attempt':i,'reason':why,'candidate':cand})
  rec['phase2_restarts']=rest;rec['phase2_restart_count']=len(rest);rec['canonical_r']=r
  if r is None:raise RuntimeError('R_VALIDATION_FAILED')
  bid=f'B-{seed_id}';sha=hashlib.sha256((a+'\n---R---\n'+r).encode()).hexdigest();producer=f'producer::{seed_id}'
  registry={bid:{'producer_subject_id':producer,'bundle_sha256':sha}};rec['bundle_id']=bid;rec['bundle_sha256']=sha
  def do(prompt,current,unspec,arm,fam):
   text,integ=tool_call(prompt,registry=registry,bundle_id=bid,current_id=current,unspecified=unspec,model=model,base=base,key=key);integ.update({'arm':arm,'family':fam});rec['tool_integrity'].append(integ);z=scored(text)
   if not z['parse_valid']:raise RuntimeError('UNPARSED_OPTION')
   return z
  for arm in PRIMARY:
   current=producer if arm.startswith('SAME') else f'other::{seed_id}'; rr=r if arm.endswith('+REFL') else None;rec['primary'][arm]={}
   for fam in ('related','unrelated'):rec['primary'][arm][fam]=do(tool_prompt(a,rr,bid,s[fam]),current,False,arm,fam)
  for arm in PLACEBO:
   rr=r if arm.endswith('+REFL') else None;rec['placebo'][arm]=do(tool_prompt(a,rr,bid,s['related']),f'null::{seed_id}',True,arm,'related')
  for arm in LABEL:
   z=scored(plain([{'role':'user','content':label_prompt(arm,a,r,s['related'])}],model,base,key));rec['label_controls'][arm]=z
   if not z['parse_valid']:raise RuntimeError('UNPARSED_OPTION')
  for name,own,current in (('CLAIM_OWN_TOOL_OTHER',True,f'other::{seed_id}'),('CLAIM_OTHER_TOOL_SAME',False,producer)):rec['conflict'][name]=do(conflict_prompt(own,a,r,bid,s['related']),current,False,name,'related')
  if seed_id in CAL:
   for arm in PRIMARY:
    current=producer if arm.startswith('SAME') else f'other::{seed_id}';rr=r if arm.endswith('+REFL') else None;rec['calibration'][arm]=do(tool_prompt(a,rr,bid,s['related']),current,False,'CAL:'+arm,'related')
 except Exception as e:
  code=str(e) if str(e) in {'R_VALIDATION_FAILED','UNPARSED_OPTION','TOOL_CALL_MISSING','TOOL_CALL_INVALID_ARGUMENT','TOOL_RESULT_MISMATCH','TOOL_PROTOCOL_FAILURE'} else 'PROVIDER_RUNTIME_FAILURE'
  rec['excluded']=True;rec['exclusion_code']=code;rec['errors'].append({'type':type(e).__name__,'message':str(e)})
 finally:
  rec['finished_unix']=time.time();write(rec,path)
 return rec
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--seed',default='P003-001');ap.add_argument('--attempt',type=int,default=1);x=ap.parse_args();run(x.seed,x.attempt)
