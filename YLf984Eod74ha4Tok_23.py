
def leap_year(yr):
  return yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0)

