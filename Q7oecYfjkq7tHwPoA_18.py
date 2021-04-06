
from math import ceil
​
def climb(stamina, obs):
  ans = 0
  for n, _ in enumerate(obs[:-1]):
    cost = obs[n+1] - obs[n]
    cost = ceil(abs(cost)) * (2 if cost > 0 else 1)
    if stamina - cost >= 0: 
      ans += 1
      stamina -= cost
    else: return ans
  return ans

