
def day_amount(month, year):
  if month == 2:
    if year % 4 == 0:
      if year % 100 == 0 and year % 400 != 0:
        return 28
      elif year % 400 == 0:
        return 29
      elif year % 100 != 0:
        return 29
    else:
      return 28
  elif month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  else:
    return 30

