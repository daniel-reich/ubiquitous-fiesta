
from datetime import timedelta, time, datetime, date
​
def bed_time(*times):
  return [go_to_sleep(*time) for time in times]
  
def go_to_sleep(alarm_time, sleep_time):
  hours, minutes = sleep_time.split(":")
  hours, minutes = int(hours), int(minutes)
  delta_time = timedelta(hours=hours, minutes=minutes)
  
  hours, minutes = alarm_time.split(":")
  hours, minutes = int(hours), int(minutes)
  alarm_time = time(hour=hours, minute=minutes)
  
  sleep_time = (datetime.combine(date(3,3,3), alarm_time) - delta_time).time()
  
  return "{:02d}:{:02d}".format(sleep_time.hour, sleep_time.minute)

