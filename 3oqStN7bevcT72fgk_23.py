
from datetime import datetime
import calendar
def get_day(day):
  day = datetime.strptime(day, '%m/%d/%Y')
  return calendar.day_name[day.weekday()]

