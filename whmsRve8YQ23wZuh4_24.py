
import datetime
def sort_dates(lst, mode):
  a = '%d-%m-%Y_%H:%M'
  if mode == 'ASC':
    mode = False
  else:
    mode = True
  return sorted(lst, key = lambda x : datetime.datetime.strptime(x,a), reverse = mode)

