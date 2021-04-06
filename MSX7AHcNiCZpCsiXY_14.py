
import datetime
def how_unlucky(y):
  return  sum(datetime.datetime(y, month, 13).weekday() == 4 for month in range(1, 13))

