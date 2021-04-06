
from itertools import accumulate, count, islice
​
def pyramidal_string(strg, typ):
  def lc(l):
    a = accumulate(count(1,1))
    return l in islice(a,0,r+1)
​
  def sl():
    c = accumulate(count(0,1))
    d = accumulate(count(1,1))
    while True:
      yield slice(next(c),next(d))
​
  t = {"REG":1, "REV":-1}.get(typ)
  l = list(strg)[::t]
  n = len(l)
  r = int(((1+n*8)**.5-1)/2)
  s = sl()
​
  if lc(n):
    return [" ".join(l[next(s)][::t]) for i in range(r)][::t]
  else:
    return "Error!" if n>1 else []

