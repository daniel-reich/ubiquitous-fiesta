
import datetime
def sort_dates(lst, mode):
  a = sorted(lst , key=lambda x: datetime.datetime.strptime(x, '%d-%m-%Y_%H:%M'))
  return a if mode=="ASC" else a[::-1]

