
def leap_year(yr):
  return yr%400 == 0 if not yr%100 else yr%4 == 0

