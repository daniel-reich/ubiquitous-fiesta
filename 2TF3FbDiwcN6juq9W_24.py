
from datetime import datetime as dt
def days_until_2021(date):
  diff = dt(2021,1,1) - dt.strptime(date,'%m/%d/%Y')
  return '{} days'.format(diff.days) if diff.days != 1 else '1 day'

