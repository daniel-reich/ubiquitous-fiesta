
import math
def check_square_and_cube(lst):
  x = math.sqrt(lst[0])
  if x * x == lst[0] and x * x * x == lst[1]:
    return True
  else: 
    return False

