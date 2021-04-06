
from datetime import date
def easter_date(y):
  M = ['January','February','March','April','May','June','July','August','September','October','November','December']
  d = calc_easter(y)
  return M[d.month-1]+' '+str(d.day)
​
def calc_easter(year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return date(year, month, day)

