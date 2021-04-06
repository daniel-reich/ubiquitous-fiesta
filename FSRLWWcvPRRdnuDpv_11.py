
from datetime import datetime, timedelta
import re
​
BREAKFAST = datetime(2000,1,2,7)
LUNCH = datetime(2000,1,2,12)
DINNER = datetime(2000,1,2,19)
​
def time_to_eat(current_time):
  match = re.search(r"(\d\d?):(\d\d?) ([ap])\.m\.", current_time)
​
  if match:
    if match.group(3)=="a":
      if match.group(1) != "12":
        dt_current = datetime(2000,1,2,int(match.group(1)),
                        int(match.group(2)))
      else:
        dt_current = datetime(2000,1,2,0, int(match.group(2)))
    else:
      dt_current = datetime(2000,1,2,int(match.group(1)) + 12,
                      int(match.group(2)))
    
    if bool(dt_current > DINNER) != bool(dt_current <= BREAKFAST):
      if dt_current > DINNER:
        dt_current = datetime(2000,1,1, dt_current.hour, dt_current.minute)
      time_diff = BREAKFAST - dt_current
    elif dt_current > BREAKFAST and dt_current <= LUNCH:
      time_diff = LUNCH - dt_current
    else:
      time_diff = DINNER - dt_current
​
    hours = divmod(time_diff.seconds, 3600)
    seconds = hours[1] / 60
    return [hours[0], seconds]

