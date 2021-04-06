
import datetime as dt
def how_unlucky(y):
  return sum(dt.datetime(y, m, 13).weekday() == 4 for m in range(1, 13))

