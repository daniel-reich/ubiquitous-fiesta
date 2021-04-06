
def is_leap(year):
  return not bool(year % 400) or ( not bool(year % 4) and bool(year % 100) )

