
def bed_time(*times):
  MINUTES_IN_DAY = 60*24
  sleep = []
  for time in times:
    wake, duration = map(to_minutes, time)
    s = (wake - duration) % MINUTES_IN_DAY
    sleep.append(to_time(s))
  return sleep
​
def to_minutes(time):
  hours, minutes = time.split(':')
  return 60*int(hours) + int(minutes)
  
def to_time(minutes):
  hours, mins = (str(t).zfill(2) for t in divmod(minutes,60))
  return '{}:{}'.format(hours, mins)

