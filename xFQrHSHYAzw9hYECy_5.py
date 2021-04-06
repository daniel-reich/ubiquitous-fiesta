
from re import split
​
def is_long_pressed(o, t):
  count = lambda s: {c: s.count(c) for c in list(set(s))}
  chunk = lambda s: ''.join(filter(bool, split("(.)\\1+", s)))
  x, y = list(filter(bool, split("\\b", o))), list(filter(bool, split("\\b", t)))
  for i, k in enumerate(x):
    a, b, w, v = chunk(x[i]), chunk(y[i]), count(x[i]), count(y[i])
    if a != b or len(a) != len(b) or any(w[k] > v[k] for k in w.keys()): return False
  return True

