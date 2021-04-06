
def how_unlucky(y):
  import datetime as dt
  return sum([dt.date(y,m,13).weekday() == 4 for m in range(1, 12+1)])

