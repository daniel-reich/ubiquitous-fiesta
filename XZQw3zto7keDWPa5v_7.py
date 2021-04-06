
def day_amount(month, year):
  if month == 2:
    return 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28
  return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30

