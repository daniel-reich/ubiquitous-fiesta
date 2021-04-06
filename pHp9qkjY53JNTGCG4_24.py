
import math
​
def century_from_year(year):
  cent = year // 100
  if year%100 != 0:
    cent +=1
  return cent

