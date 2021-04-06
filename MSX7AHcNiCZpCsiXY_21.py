
from datetime import date
def how_unlucky(y):
  count = 0
  for m in range(1,13):
    try:
      count += date(y,m,13).weekday() == 4
    except ValueError:
      pass
  return count

