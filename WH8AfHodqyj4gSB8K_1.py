
import re
def is_authentic_skewer(s):
  f=lambda i,j:i not in v and j not in v
  if'-'not in s:return 0
  v,l='AEIOU',s.split(re.search('[-]+',s).group(0))
  return f(l[0],l[-1])and 1-any(len(x)-len(y)or x in v and y in v or f(x,y)for x,y in zip(l,l[1:]))

