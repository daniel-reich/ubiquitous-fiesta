
import datetime
​
def week_after(d):
    d, m, y = d.split('/')
    d1 = datetime.date(int(y), int(m), int(d)) + datetime.timedelta(days=7)
    return "{:>02}/{:>02}/{}".format(d1.day,d1.month,d1.year)

