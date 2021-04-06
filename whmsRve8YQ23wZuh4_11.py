
from datetime import datetime
def sort_dates(lst, mode):
  to=[datetime.strptime(x, '%d-%m-%Y_%H:%M') for x in lst]
  if (mode=="ASC"):
    to.sort()
    return [datetime.strftime(i, '%d-%m-%Y_%H:%M') for i in to]
  else:
    to.sort(reverse=True)
    return [datetime.strftime(j, '%d-%m-%Y_%H:%M') for j in to]

