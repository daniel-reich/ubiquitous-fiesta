
import datetime
​
​
def first_tuesday_of_the_month(year, month):
    d = datetime.datetime(year, month, 1)
    offset = 1-d.weekday()  # weekday = 1 means tuesday
    if offset < 0:
        offset += 7
    x = d+datetime.timedelta(offset)
    return str(x.date())

