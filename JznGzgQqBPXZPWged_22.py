
import re
def resist(net):
  s=r'\([\d+\.?\,\s]+\)'
  p=p=r'\[[\d+\.?\,\s]+\]'
  while '(' in net or '[' in net:
    if bool(re.search(s,net)):
      net=re.sub(s, lambda m: str(sum(eval(m.group(0)))), net)
    else:
      net=re.sub(p, lambda m: str(1/sum( 1/x for x in eval(m.group(0)))), net)
  return round(eval(net),1)

