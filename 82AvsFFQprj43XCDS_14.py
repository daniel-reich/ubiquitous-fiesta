
import re
def no_strangers(txt):
  ws = re.findall(r"\b[\w']+\b",txt.lower())
  aq = [ws[i] for i in range(len(ws)) if ws[:i].count(ws[i])==2 and ws.count(ws[i])<5]
  fr = [ws[i] for i in range(len(ws)) if ws[:i].count(ws[i])==4]
  return [aq,fr]

