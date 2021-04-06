
import math
def lcm_three(num):
  cond = False
  i = 1
  while not cond:
    if (max(num)*i)%num[0]!=0 or (max(num)*i)%num[1]!=0 or (max(num)*i)%num[2]!=0:
      i+=1
    elif (max(num)*i)%num[0]==0 and (max(num)*i)%num[1]==0 or (max(num)*i)%num[2]==0:
      cond = True
  return max(num)*i

