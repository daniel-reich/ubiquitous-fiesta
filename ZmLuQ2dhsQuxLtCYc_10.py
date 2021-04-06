
from datetime import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  start_date = datetime.strptime(start_date,"%Y,%m,%d")
  end_date = datetime.strptime(end_date,"%Y,%m,%d")
  if start_date>end_date:
    return "Invalid date"
  if start_read>end_read:
    return "Invalid meter readings"
  days = ((end_date-start_date).days)*stand
  units = (end_read-start_read)*tariff
  total = days+units
  return "${0}".format(round(total+total*0.05,2))

