
import re
def is_match(s, p):
  t=s*2
  p=r'{}'.format(p)
  if '*' not in p and '.' not in p:
    return re.match(s,t).group()==re.match(p,t).group()
  else:
    return bool(re.match(p,s))

