
from datetime import date
def how_unlucky(y):
  return sum([1 for x in range(1,13) if date(y,x,13).strftime('%a')=='Fri'])

