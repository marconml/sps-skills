"""Exercise management-copy QA across prose, insights, headings and methodology."""
from pathlib import Path
import subprocess,sys,tempfile
script=Path(__file__).resolve().parents[1]/'scripts/editorial_voice_qa.py'
examples=[
 ('<li>完整輪播均已核對，判斷來自卡片而非caption。</li>',False),
 ('<h3>All carousel cards have been inspected</h3>',False),
 ('<p>Identity is checked against the incident details.</p>',False),
 ('<h3>封面先見食物，再講比較結果</h3><li>產品近鏡讓價錢容易比較，仍有低反應反例。</li>',True),
 ('<details id="methodology"><p>All carousel cards have been inspected.</p></details>',True),
]
with tempfile.TemporaryDirectory() as folder:
 for i,(body,valid) in enumerate(examples):
  p=Path(folder)/f'{i}.html';p.write_text('<html><body>'+body+'</body></html>')
  result=subprocess.run([sys.executable,str(script),str(p)],capture_output=True,text=True)
  assert (result.returncode==0)==valid,(body,result.stdout,result.stderr)
print('PASS: process leakage rejected in narrative, insight and heading; findings and methodology accepted')
