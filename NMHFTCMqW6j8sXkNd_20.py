
def check_square_and_cube(lst):
  sr1 = lst[0]**(1/2)
  cr2 = lst[1]**(1/3)
  return abs(sr1-cr2) <= 0.000001

