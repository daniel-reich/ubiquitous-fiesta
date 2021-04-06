
import datetime
​
def how_unlucky(y):
  return sum([1 for m in range(1,13) if datetime.datetime(y,m,13).strftime("%A") == "Friday"])

