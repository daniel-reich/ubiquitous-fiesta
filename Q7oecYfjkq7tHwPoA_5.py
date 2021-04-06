
from math import *
def climb(st, obs):
  x = 0
  while st >= 0:
    if len(obs) < 2: return x
    diff = obs[1] - obs.pop(0)
    st -= max([ceil(diff),-floor(diff)]) * (1+(diff>0)); x += 1
  return x - 1

