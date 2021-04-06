
import datetime
def first_tuesday_of_the_month(year, month): 
    x = datetime.datetime(year,month,1)
    day = datetime.timedelta(days=1)
    while x.date().weekday() != 1:
        x = x + day 
    return '{:04d}-{:02d}-{:02}'.format(x.date().year,x.date().month,x.date().day)

