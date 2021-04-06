
import datetime
def sort_dates(lst, mode):
  if mode=='ASC':
    return sorted(lst,key=lambda x: datetime.datetime.strptime(x, '%d-%m-%Y_%H:%M'))
  if mode=='DSC':
    return sorted(lst,key=lambda x: datetime.datetime.strptime(x, '%d-%m-%Y_%H:%M'),reverse=True)

