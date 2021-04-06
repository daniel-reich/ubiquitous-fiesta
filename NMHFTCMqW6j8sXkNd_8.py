
from math import sqrt 
def check_square_and_cube(lst):
  print(sqrt(lst[0]) ,lst[1]**(1 / 3))
  return sqrt(lst[0]) == round(lst[1]**(1 / 3),2)

