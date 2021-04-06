
from datetime import datetime
def sort_dates(lst, mode):
  L = sorted(lst, key = lambda x : datetime.strptime(x, '%d-%m-%Y_%H:%M'))
  return L if mode == 'ASC' else list(reversed(L))

