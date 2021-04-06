
from datetime import date
def how_unlucky(y):
  count = 0 
  for i in range(1, 13):
    if date(y, i, 13).weekday() == 4:
      count +=1
  return count

