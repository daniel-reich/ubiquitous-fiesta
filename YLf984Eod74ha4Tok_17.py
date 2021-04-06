
def leap_year(yr):
  return any([all([yr % 4 == 0, not yr % 100 == 0]), yr % 400 == 0])

