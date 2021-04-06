
import datetime
def add_n_days_to_a_date(date, days):
    s = ''
    x = datetime.datetime(int(date[4:]), int(date[2:4]),int(date[:2])) + datetime.timedelta(days = days)
    if x.day < 10:
        s += '0' + str(x.day)
    else:
        s += str(x.day)
    if x.month < 10:
        s += '0' + str(x.month)
    else:
        s += str(x.month)
    s += str(x.year)
    return s

