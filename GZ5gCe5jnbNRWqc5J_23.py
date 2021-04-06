
from datetime import datetime
​
​
def first_tuesday_of_the_month(year, month):
    d = datetime(year, month, 1)
    for x, i in enumerate(range(8), 1):
        d = d.replace(day=x)
        if d.weekday() == 1:
            return d.strftime("%Y-%m-%d")

