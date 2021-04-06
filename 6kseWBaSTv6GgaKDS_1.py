
from re import search, findall
​
def next_letters(x):
  if not len(x): return 'A'
  if search(r'Z\Z', x) is None:
    return x[:-1] + chr(ord(x[-1])+1)
  else:
    r = findall(r'[A-Y]?Z+\Z', x)[0]
    t = ''.join('A' if a == 'Z' else chr(ord(a)+1) for a in r)
    return t + 'A' if len(t) == len(x) else x[:-len(r)] + t

