
import re
def find_longest(s,w=''):
  if not s:return w
  t=re.search(r'\w+',s.lower())
  if t:t=t.group(0)
  if len(t)>len(w):w=t
  return find_longest(s[len(t)+1:],w)

