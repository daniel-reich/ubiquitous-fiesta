
import math
​
def century_from_year(year):
  if year%100 == 0:
    return year//100
  else:
    return 1+(year//100)

