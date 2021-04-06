
import re
def find_pattern(d, p):
  p='(?i)'+p
  res=[]
  for x in d:
    if bool(re.search(p, d[x])):
      res.append('{} = {}'.format(x, re.search(p, d[x]).group()))
    else:
      res.append('{} = {}'.format(x, None))
  return sorted(res)

