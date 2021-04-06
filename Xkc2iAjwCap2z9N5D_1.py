
from datetime import date
def has_friday_13(month, year):
  return date(year,month,13).strftime("%A")=='Friday'

