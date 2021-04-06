
from re import finditer
def compress(c):
  m = [''.join(c[x.start():x.end()]) for x in finditer(r'(\w)\1*', ''.join(c))]
  return ''.join(s[0] + ('' if len(s) < 2 else str(len(s))) for s in m)

