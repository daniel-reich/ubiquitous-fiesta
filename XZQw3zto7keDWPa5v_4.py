
def day_amount(month, year):
  from calendar import monthrange
  tupla = monthrange(year,month)
  return tupla[1]

