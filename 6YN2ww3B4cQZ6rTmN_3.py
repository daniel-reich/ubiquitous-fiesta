
def leapYear(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0: # year % 4 != 0 is false so it is a multiple of 4
    return True
  elif year % 400 != 0: # year % 100 != 0 is false so it is a multiple of 100
    return False

