
import math
​
def is_heteromecic(c):
  if c==1 or c==0: 
    return True
  x,y=math.ceil(c**(0.5)),math.floor(c**(0.5))
  return x*y==c and is_heteromecic(abs(x-y))

