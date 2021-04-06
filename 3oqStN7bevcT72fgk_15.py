
import datetime
import calendar
​
def get_day(day):
  return calendar.day_name[datetime.datetime.strptime(day, '%m/%d/%Y').weekday()]

