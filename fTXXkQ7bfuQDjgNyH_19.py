
from datetime import datetime as dt
def day_of_year(date):
  return int(dt.strptime(date,'%m/%d/%Y').strftime('%j'))

