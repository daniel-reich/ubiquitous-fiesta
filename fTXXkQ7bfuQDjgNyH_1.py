
from datetime import datetime as dt
def day_of_year(date):
    d = dt.strptime(date, "%m/%d/%Y")
    return (d - dt(year=d.year - 1, month=12, day=31)).days

