
import math
​
def century_from_year(year):
    if year<=100:
      return 1
    elif year%100==0 and year%1000!=0:
      return year/100
    elif year%100!=0 or year%1000==0:
      return int(year / 100) + 1

