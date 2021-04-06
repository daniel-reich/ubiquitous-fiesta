
def leap_year(year):
  total = year % 4 == 0
  total1 = total % 100 == 0
  if total == False:
    return False
  else:
    return True

