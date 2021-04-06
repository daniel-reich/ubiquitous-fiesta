
import datetime as dt
def days_between_dates(d1, d2):
  dt1=dt.datetime.strptime(d1, "%d%m%Y")
  dt2=dt.datetime.strptime(d2, "%d%m%Y")
  td=dt2-dt1
  return abs(td.days)

