
from datetime import datetime, timedelta
def week_after(d):
  f = '%d/%m/%Y'
  d = datetime.strptime(d,f)
  d_week = d + timedelta(days=7)
  return d_week.strftime(f)

