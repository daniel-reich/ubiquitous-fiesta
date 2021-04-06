
import math
def climb(sta,obs):
  for o in range(1,len(obs)):
     if (obs[o]-obs[o-1])<0:
         sta= sta-math.ceil(abs(obs[o]-obs[o-1]))*1
     else:
         sta = sta - math.ceil(abs(obs[o] - obs[o - 1]))*2
     if sta<0: return o-1
     elif sta==0: return o
​
  return o

