
import datetime
​
def days_until_2021(date):
    m, d, y = date.split('/')
    dt = datetime.date(int(y), int(m), int(d))
    days = (datetime.date(2021, 1, 1) - dt).days
    if days > 1:
        return str(days) + ' days'
    return str(days) + ' day'

