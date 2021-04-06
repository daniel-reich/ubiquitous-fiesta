
import re, datetime
​
def sync_subs(subtitles, timeIncrement):
  regex = r'\d{2}:\d{2}:\d{2},\d{3}'
  async = re.findall(regex, subtitles)
  incr = ','.join(timeIncrement.split(':')).split(',')
  if not re.match(regex, timeIncrement):
    return 'There is a problem with the second argument'
  else:
    for i in range(3):
      if not 0 <= int(incr[i]) <= 59:
        return 'There is a problem with the second argument'
    if not 0 <= int(incr[3]) <= 999:
      return 'There is a problem with the second argument'
    incrTime = datetime.timedelta(hours=int(incr[0]), minutes=int(incr[1]), seconds=int(incr[2]), microseconds=int(incr[3]))
    b = subtitles
    for time in async:
      a = ','.join(time.split(':')).split(',')
      aTime = datetime.timedelta(hours=int(a[0]), minutes=int(a[1]), seconds=int(a[2]), microseconds=int(a[3]))
      newTime = aTime + incrTime
      s, msec = divmod(newTime.microseconds, 1000)
      minut, sec = divmod(newTime.seconds+s, 60)
      hours, minutes = divmod(minut, 60)
      b = re.sub(time, '{:02}:{:02}:{:02},{:03}'.format(hours,minutes,sec,msec), b)
    return b

