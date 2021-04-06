
from _datetime import datetime
import calendar
def get_day(day):
    day = datetime.strptime(day.replace('/', '-'), '%m-%d-%Y' )
    return calendar.day_name[day.weekday()]

