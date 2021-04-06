
from datetime import datetime as dt
def leap_year(yr):
    try:
        x = dt(year=yr, month=2, day=29)
        return True
    except:
        return False

