
import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  d,r=(datetime.datetime.strptime(end_date,"%Y,%m,%d")-datetime.datetime.strptime(start_date,"%Y,%m,%d")).days,end_read-start_read
  if d<0:
    return "Invalid date"
  elif r<0:
    return "Invalid meter readings"
  return "${:0.2f}".format((d*stand+r*tariff)*1.05)

