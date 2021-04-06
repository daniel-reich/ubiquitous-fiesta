
def day_amount(month, year):
  if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    return 29
  elif month == 2:
    return 28
  elif month != 2 and month % 2 == 0 and month < 7:
    return 30
  elif (month != 2 and month % 2 == 0 and month > 7) or (month % 2 != 0 and month <= 7):
    return 31
  else:
    return 30

