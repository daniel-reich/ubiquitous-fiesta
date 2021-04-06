
import re
def find_longest(s):
  p=r'\w+'
  if not bool(re.search(p, s)):
    return ''
  else:
    k=re.search(p,s).group()
    return max(k, find_longest(re.sub(k,'',s)), key=len).lower()

