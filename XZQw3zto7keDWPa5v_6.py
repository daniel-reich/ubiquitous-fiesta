
from calendar import monthrange
def day_amount(month, year):
  x = monthrange(year, month)
  return(x[1])

