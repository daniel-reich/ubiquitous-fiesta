
def leap_year(yr):
  #condition1: divisible by 4
  #condition2: divisible by 100:
  #condition3: divisible by 400:
  c2 = {True:bool(yr % 400 == 0),False:True}
  c1 = {True:c2[bool(yr % 100 == 0)], False:False}
  return c1[bool(yr % 4 == 0)]

