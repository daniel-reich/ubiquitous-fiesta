
from datetime import datetime
def get_day(day):
  date = datetime.strptime(day, '%m/%d/%Y')
  weekday = date.strftime('%A')
  return weekday

