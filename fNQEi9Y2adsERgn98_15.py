
def perimeter(lst):
  from math import sqrt
  s1 = sqrt(abs(lst[0][0] - lst[1][0])**2 + abs(lst[0][1] - lst[1][1])**2)
  s2 = sqrt(abs(lst[0][0] - lst[2][0])**2 + abs(lst[0][1] - lst[2][1])**2)
  s3 = sqrt(abs(lst[1][0] - lst[2][0])**2 + abs(lst[1][1] - lst[2][1])**2)
  return float('{:.2f}'.format(s1 + s2 + s3))

