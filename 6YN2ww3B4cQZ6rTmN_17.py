
def leapYear(year):
  return True if year % 100 == 0 or year % 400 and year % 4 == 0 else False

