
import datetime as d
​
def has_friday_13(month, year):
    x = d.datetime(year, month, 13)
    y = x.strftime("%A")
    if y == "Friday":
        return True
    else:
        return False

