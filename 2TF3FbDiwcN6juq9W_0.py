
from datetime import datetime
def days_until_2021(date):
  enddate = datetime(2021, 1, 1)
  startdate = datetime.strptime(date, "%m/%d/%Y")
  days = (enddate - startdate).days
  return '{} day{}'.format(days, ['', 's'][days>1])

