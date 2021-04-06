
import datetime as d
def sort_dates(lst, mode):
  result = []
  result1 = []
  for i in lst:
    year = int(i[6:10])
    month = int(i[3:5])
    date = int(i[:2])
    hour = int(i[11:13])
    min = int(i[14:])
    sec = 0
    milsec = 0
    result.append(d.datetime(year, month, date, hour, min, sec, milsec))
  if mode == 'ASC':
    result.sort()
  else:
    result.sort(reverse=True)
  for j in result:
    d1 = str(j.day) if len(str(j.day))>1 else '0'+str(j.day)
    m1 = str(j.month) if len(str(j.month))>1 else '0'+str(j.month)
    y1 = str(j.year)
    h1 = str(j.hour) if len(str(j.hour))>1 else '0'+str(j.hour)
    mi1 = str(j.minute) if len(str(j.minute))>1 else '0'+str(j.minute)
    result1.append(d1+'-'+m1+'-'+y1+"_"+h1+':'+mi1)
  return result1

