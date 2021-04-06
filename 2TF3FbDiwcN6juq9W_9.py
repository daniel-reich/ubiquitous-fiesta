
from datetime import datetime
def days_until_2021(date):
  new_year = datetime(2021,1,1)
  date = datetime.strptime(date, "%m/%d/%Y")
  days = (new_year - date).days
  return '{} day{}'.format(days, 's'*(days!=1))

