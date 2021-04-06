
import math
def climb(stamina, obs):
  cleared = 0
  for i in range(len(obs)-1):
    if obs[i] < obs[i+1]:
      stamina -= 2*math.ceil(obs[i+1]-obs[i])
    else:
      stamina -= math.ceil(obs[i]-obs[i+1])
    if stamina <0:
        break
    else:
      cleared+= 1
  return cleared

