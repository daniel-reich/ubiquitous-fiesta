
from math import ceil
def climb(stamina, obs):
  i = 0
  while i < len(obs)-1:
    if obs[i+1] > obs[i]:
      st = 2*(ceil(obs[i+1]-obs[i]))
    else:
      st = ceil(obs[i]-obs[i+1])
    stamina -= st
    if stamina < 0:
      break
    i += 1
  return i

