
from datetime import datetime
def sort_dates(lst, mode):
  lst.sort(key = lambda d: datetime.strptime(d, '%d-%m-%Y_%H:%M'))
  return lst[::1 if mode is 'ASC' else -1]

