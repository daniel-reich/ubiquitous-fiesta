
from datetime import datetime
​
def sort_dates(lst, mode):
  as_dt = lambda date: datetime.strptime(date, '%d-%m-%Y_%H:%M')
  return sorted(lst, key=as_dt, reverse=mode=='DSC')

