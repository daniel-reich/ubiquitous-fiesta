
def sort_dates(lst, mode):
  import datetime
  import numpy as np
  date_obj = []
  for date in lst:
    day, month, year = date.split("-")
    year, time = year.split('_')
    hour, minute = time.split(':')
    date_obj.append(datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute)))
  sorted = np.argsort(date_obj).tolist()
  result = []
  for i in range(len(lst)):
    result.append(lst[sorted[i]])
  if mode=="DSC":
    return result[::-1]
  return result

