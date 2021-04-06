
import datetime
​
def week_after(d):
    day, month, year = [int(_) for _ in d.split("/")]
    now = datetime.datetime(year, month, day)
    later = now + datetime.timedelta(days=7)
    return str(later.day).zfill(2) + "/" + str(later.month).zfill(2) + "/" + \
           str(later.year)

