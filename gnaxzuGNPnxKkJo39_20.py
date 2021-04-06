
from datetime import date
def easter_date(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    m = f // 31
    day = f % 31 + 1    
    month = date(y, m, day).strftime('%B')
    return month + ' ' + str(day)

