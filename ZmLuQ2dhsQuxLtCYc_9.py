
import datetime
​
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  start_date = datetime.datetime.strptime(start_date, "%Y,%m,%d")
  end_date = datetime.datetime.strptime(end_date, "%Y,%m,%d")
​
  days = (end_date - start_date).days
  if days < 0: return "Invalid date"
​
  bill = end_read - start_read
  if bill < 0: return "Invalid meter readings"
​
  bill = bill * tariff + days * stand
  bill *= 1.05
​
  return "$%.02f" % bill

