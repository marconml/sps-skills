"""Canary for explicit profile chapter contracts; no production data."""
import json,subprocess,sys,tempfile
from pathlib import Path
script=Path(__file__).resolve().parents[1]/'scripts/validate_report.py'
def check(profile,sections,expected):
 html='<html><head><title>Fixture</title></head><body data-default-language="en"><h1>Fixture</h1><div data-language-toggle><button data-lang-option="en">EN</button><button data-lang-option="zh">ZH</button></div><script data-bilingual-report></script>'
 html+=''.join('<section id="'+s+'"></section>' for s in sections)
 html+='<div data-module="page-scorecard"></div><div data-module="core-pillar-comparison"></div><a href="https://www.facebook.com/example">Example</a></body></html>'
 with tempfile.TemporaryDirectory() as d:
  p=Path(d)/'fixture.html';p.write_text(html);r=subprocess.run([sys.executable,str(script),str(p),'--profile',profile],capture_output=True,text=True);out=json.loads(r.stdout);assert out['status']==expected,(profile,sections,out)
check('default',['scope','movement','drivers','actions','methodology'],'PASS')
check('healthy-days',['scope','movement','drivers','outlook','methodology'],'PASS')
check('healthy-days',['scope','drivers','movement','outlook','methodology'],'FAIL')
check('healthy-days',['scope','movement','drivers','methodology'],'FAIL')
print('PASS: default and Healthy Days profile reading paths, missing and reordered chapters')
