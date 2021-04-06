
def how_unlucky(y):
  from datetime import datetime as dt
  return sum(dt(y, i, 13).weekday()==4 for i in range(1,13))

