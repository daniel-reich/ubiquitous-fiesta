
import re
def is_authentic_skewer(s):
  v = lambda x: x in 'AEIOU'
  sep = re.findall('[^\w]+',s)
  if v(s[0]) == v(s[-1]) == False:
    if len(set(sep)) == 1:
      s = s.split(sep[0])
      if all(len(i)==1 for i in s):
        return all(v(a)!=v(b) for a, b in zip(s,s[1:]))
  return False

