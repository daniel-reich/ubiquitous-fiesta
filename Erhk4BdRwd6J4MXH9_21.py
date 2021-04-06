
def is_leap(year):
  if year % 400 == 0:
    return True
  else:
    if year % 4 == 0 and year % 100 != 0:
      return True
    else:
      return False

