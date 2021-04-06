
import time
import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  d1 = time.mktime(datetime.datetime.strptime(end_date, "%Y,%m,%d").timetuple())
  d2 = time.mktime(datetime.datetime.strptime(start_date, "%Y,%m,%d").timetuple())
  diff = round((d1 - d2) / 86400)
  meter = end_read - start_read
  amount = diff * stand + meter * tariff
  return "${}".format(round(amount + amount * 0.05, 2)) if diff >= 0 and meter >= 0 else \
    "Invalid meter readings" if meter < 0 else "Invalid date"

