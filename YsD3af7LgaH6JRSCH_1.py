
from datetime import datetime, timedelta
def time_adjust(now, hrs, mins, sec):
  t = datetime.strptime(now,'%H:%M:%S') + timedelta(hours=hrs,minutes=mins,seconds=sec)
  return t.strftime('%H:%M:%S')

