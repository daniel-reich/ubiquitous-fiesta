
import datetime
​
def has_friday_13(month, year):
    d = datetime.datetime(year, month, 13)
    return int(d.strftime('%w')) == 5
​
    print(has_friday_13(10, 2020))

