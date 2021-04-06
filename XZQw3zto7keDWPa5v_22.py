
from calendar import monthrange
def day_amount(month, year):
  return list(monthrange(year,month))[1]

