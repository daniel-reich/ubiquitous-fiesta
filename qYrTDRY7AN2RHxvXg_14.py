
from math import sqrt
def f(A, c):
  
  try:
    y = sqrt((c**2 - sqrt(c**4 - 16*A**2))/2)
  except:
    return "Does not exist"
  x = 2*A/y
  
  
  l = sorted([x,y])
  
  return [round(l[0],3),round(l[1],3)]

