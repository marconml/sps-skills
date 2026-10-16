#!/usr/bin/env python3
"""Flag editorial-copy workflow leaks. Semantic depth still requires media-led review."""
import argparse,json,re
from html.parser import HTMLParser
from pathlib import Path
class Read(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.paragraphs=[];self.current=None;self.reader=False;self.blocks=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);in_method=any(x[1].get('id')=='methodology' for x in self.stack)
  if tag not in ('img','meta','link','br','input','hr','source'):self.stack.append((tag,a))
  if a.get('id') in ('reader','part-2c'):self.reader=True
  if tag=='p':self.current={'method':in_method,'text':''}
  if tag in ('p','li','h1','h2','h3','h4'):
   self.blocks.append({'tag':tag,'method':in_method,'text':''})
 def handle_data(self,data):
  if self.current:self.current['text']+=data
  for block in self.blocks:block['text']+=data
 def handle_endtag(self,tag):
  if tag=='p' and self.current:self.paragraphs.append(self.current);self.current=None
  for i in range(len(self.blocks)-1,-1,-1):
   if self.blocks[i]['tag']==tag:
    block=self.blocks.pop(i)
    if tag!='p':self.paragraphs.append(block)
    break
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
ap=argparse.ArgumentParser();ap.add_argument('report');ap.add_argument('--comments-available',action='store_true');ap.add_argument('--video-workflow',choices=['original','repost','mixed'],default='mixed');args=ap.parse_args();p=Read();p.feed(Path(args.report).read_text());issues=[]
patterns=[r'保留作獨立.{0,12}分析',r'唔同.{0,30}(?:對比|比較)',r'keep this as a standalone.{0,20}diagnosis',r'its.{0,25}interactions are not compared',r'本案例.{0,20}(?:驗收|符合規則|完成檢查)']
patterns += [r'(?:完整|全部|所有).{0,10}(?:輪播|卡片|序列|圖片|媒體).{0,10}(?:已|均已).{0,6}(?:核對|檢查|確認|看齊)',r'(?:已核對|已看齊|已檢查|已查核).{0,12}(?:輪播|卡片|序列|圖片|原片)',r'判斷(?:來自|基於).{0,20}(?:而非|不是|唔係)\s*caption',r'(?:all|complete|full).{0,28}(?:cards|carousel|sequence|media).{0,16}(?:inspected|checked|reviewed|verified)',r'(?:identity|match).{0,15}(?:is|was|has been)\s*(?:checked|verified)']
if args.video_workflow=='repost':patterns += [r'for a hotel-led cut',r'move the music memorabilia after',r'酒店片先出房間',r'build the Reel around the journey']
for x in p.paragraphs:
 if not x['method']:
  for pat in patterns:
   m=re.search(pat,x['text'],re.I)
   if m:issues.append({'kind':'editorial_voice','match':m.group(),'paragraph':x['text'][:1000]});break
if p.reader and not args.comments_available:issues.append({'kind':'empty_reader_section','message':'No usable comment evidence: omit reader subpart and navigation.'})
print(json.dumps({'status':'FAIL' if issues else 'PASS','issues':issues,'scope':'Mechanical flags only; review all case reasoning and workflow fit against media before release.','repair':'Reassess and rewrite the affected paragraph where needed; preserve or restore media-specific reasoning rather than deleting flagged text alone.'},ensure_ascii=False,indent=2))
raise SystemExit(bool(issues))
