
from datetime import datetime as dt
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  st = dt.strptime(start_date,'%Y,%m,%d')
  end = dt.strptime(end_date, '%Y,%m,%d')
  if st > end:
    return 'Invalid date'
  days = (end-st).days
  units = end_read - start_read
  if units < 0:
    return 'Invalid meter readings'
  cost = (units*tariff + days*stand)
  return '${:.2f}'.format(cost + cost*5/100)

