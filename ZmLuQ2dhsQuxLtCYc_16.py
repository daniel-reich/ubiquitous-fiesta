
from datetime import datetime
​
​
def time_difference(start, end):
    d1 = datetime.strptime('-'.join(start.split(',')), "%Y-%m-%d")
    d2 = datetime.strptime('-'.join(end.split(',')), "%Y-%m-%d")
    return (d2 - d1).days
​
​
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  
  if end_read < start_read:
    return "Invalid meter readings"
​
  delta = time_difference(start_date, end_date)
  if delta < 0:
    return "Invalid date"
​
  bill = (end_read - start_read) * tariff + stand * delta
  bill *= 1.05
​
  return '${}'.format(round(bill, 2))

