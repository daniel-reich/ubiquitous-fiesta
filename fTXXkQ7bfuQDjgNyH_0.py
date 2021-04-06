
from datetime import date
​
def day_of_year(s):
    m, d, y = map(int, s.split('/'))
    return (date(y, m, d) - date(y, 1, 1)).days + 1

