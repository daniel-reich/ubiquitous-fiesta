
import datetime
​
def has_friday_13(month, year):
    ns = datetime.datetime(year, month, 13)
    if ns.weekday() == 4:
        return True
    else:
        return False

