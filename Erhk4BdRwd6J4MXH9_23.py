
def is_leap(year):
  return True if not year%400 or not year%4 and year%100 else False

