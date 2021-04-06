
from datetime import datetime as dt, timedelta as td
def add_n_days_to_a_date(date, days):
    return dt.strftime(dt.strptime(date, '%d%m%Y') + td(days=days), '%d%m%Y')

