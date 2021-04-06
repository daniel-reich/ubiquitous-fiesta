
from datetime import datetime
def has_friday_13(month, year):
  return datetime(year, month, 13).strftime('%a') == 'Fri'

