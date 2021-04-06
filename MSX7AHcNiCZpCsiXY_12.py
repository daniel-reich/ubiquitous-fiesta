
from datetime import datetime as dt
def how_unlucky(y):
  return sum(dt.strftime(dt(y,m,13),"%a")=="Fri" for m in range(1,13))

