
import re
def security(txt):
  s=''
  for x in txt:
    if x!='x':
      s+=x
  p=r'\$T|T\$'
  return "ALARM!" if bool(re.search(p,s)) else "Safe"

