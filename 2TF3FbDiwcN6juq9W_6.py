
from datetime import datetime as dt
def days_until_2021(date):
    n = (dt(2021, 1, 1) - dt.strptime(date, "%m/%d/%Y")).days
    return '{} day{}'.format(n, "s" if n > 1 else "")

