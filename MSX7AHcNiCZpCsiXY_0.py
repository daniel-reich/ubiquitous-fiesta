
from datetime import date
​
def how_unlucky(y):
  return sum(date(y, m, 13).strftime('%A') == 'Friday' for m in range(1, 13))

