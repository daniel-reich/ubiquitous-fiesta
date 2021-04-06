
from math import sqrt
def perimeter(lst):
  l1 = sqrt((lst[1][0]-lst[0][0])**2 + (lst[1][1]-lst[0][1])**2)
  l2 = sqrt((lst[2][0]-lst[1][0])**2 + (lst[2][1]-lst[1][1])**2)
  l3 = sqrt((lst[2][0]-lst[0][0])**2 + (lst[2][1]-lst[0][1])**2)
  return round(l1 + l2 + l3,2)

