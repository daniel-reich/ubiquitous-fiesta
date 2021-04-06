
import time
def get_day(day):
  return time.strftime("%A", time.strptime(day, "%m/%d/%Y"))

