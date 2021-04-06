
from datetime import datetime as dt
def days_between_dates(d1, d2):
    return abs((dt.strptime(d1, '%d%m%Y') - dt.strptime(d2, '%d%m%Y')).days)

