
from fractions import gcd
from functools import reduce
​
def lcm(*args):
    return reduce(lambda x, y: y * x // gcd(x, y), args)
​
def hats(lst):
  n, m = lst
  sch = m[:]
  minsPerCycle = lcm(*m)
  hatsPerCycle = sum(minsPerCycle // m[i] for i in range(len(m)))
  cycles, toMake = divmod(n, hatsPerCycle)
  made = cycles * hatsPerCycle
  mins = 0
  while made < n:
    i = sch.index(min(sch))
    mins = sch[i]
    for i in range(len(sch)):
      if (sch[i] == mins):
        made += 1
        sch[i] += m[i]
  mins += minsPerCycle * cycles
  return "{} minute{}".format(mins, 's' if mins > 1 else '') if made == n else None

