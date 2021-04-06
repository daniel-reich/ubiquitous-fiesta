
def day_amount(month, year):
  from calendar import monthrange
  return monthrange(year, month)[1]

