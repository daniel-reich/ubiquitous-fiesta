
import math as m
​
def check_square_and_cube(lst):
  this = m.sqrt(lst[0])
  
  if this ** 3 == lst[1]:
    return True
  else:
    return False

