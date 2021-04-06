
import datetime
​
def week_after(d):
    day, month, year = list(map(int ,d.split('/')))
    date = datetime.date(year, month, day)
    delta = datetime.timedelta(days=7)
    return "{2}/{1}/{0}".format(*(str(date + delta).split('-')))

