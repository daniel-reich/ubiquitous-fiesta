
import math
def largest_exponential(lst):
  v=0
  c=1
  e=0
  for l in lst:
    if l[1]*math.log(l[0])>v:
      v=l[1]*math.log(l[0])
      e=c
    c+=1
  return e

