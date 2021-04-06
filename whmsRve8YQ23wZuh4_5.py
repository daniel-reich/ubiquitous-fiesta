
from datetime import datetime
def sort_dates(lst, mode):
  sorted_dates = sorted(
      lst,
      key=lambda x: datetime.strptime(x,"%d-%m-%Y_%H:%M")
    )
  return sorted_dates if mode=='ASC' else sorted_dates[::-1]

