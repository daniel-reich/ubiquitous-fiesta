
import math
​
def century_from_year(year):
  return year/100 if year % 100 == 0 else math.ceil(year/100)

