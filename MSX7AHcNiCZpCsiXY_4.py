
import datetime
import calendar
def how_unlucky(y):
  d = 32
  m = 13
  f = []
  for i in range(1,m):
    for j in range(1,d):
      try: 
        date = datetime.date(y,i,j)
        if calendar.day_name[date.weekday()] == "Friday" and j == 13:
          f.append(date)
      except:
        pass
  return len(f)

