
import datetime as d
import calendar as c
def first_tuesday_of_the_month(year,month):
    calendar = c.Calendar(firstweekday=2)
    month = calendar.itermonthdates(year,month)
    for x in month:
        if c.day_name[x.weekday()] == 'Tuesday':
            day =d.datetime.strftime(x,'%Y-%m-%d')
            return day

