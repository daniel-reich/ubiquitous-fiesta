
import math
def pairs(lst):
  halflen=math.ceil(len(lst)/2)
  output=[]
  if halflen==0: return output
  for i in range(halflen):
    output.append([lst[i],lst[-i-1]])
  return output

