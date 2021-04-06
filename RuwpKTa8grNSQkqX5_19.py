
def fractions(decimal):
  import re
  s = float(re.sub(r'(\(|\))','',decimal))
  q = int(re.sub(r'(\(|\)|\.)','',decimal))
  y = len(re.findall(r'\.[\d]*\(', decimal)[0])-2
  x = (len(re.findall(r'[\(][\d]+[\)]', decimal)[0]) - 2) + y
  c = b = int(10 ** x - 10 ** y, )
  d = a = int(q - int(s * 10 ** y),)
  while c:
      d, c = c, d % c
  return '{}/{}'.format(int(a // d,), int(b // d,)) if d != 1 else '{}/{}'.format(a, b)

