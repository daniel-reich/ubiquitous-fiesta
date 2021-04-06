
import re
import datetime
import time
​
def sync_subs(subtitles, timeIncrement):
​
  match=re.compile(r"\d\d:\d\d:\d\d,\d\d\d")
​
  try:
      time.strptime(timeIncrement.replace(",",":")+"000","%H:%M:%S:%f")
  except ValueError:
      return "There is a problem with the second argument"
​
  add_hours=int(timeIncrement[:2])
  add_minutes=int(timeIncrement[3:5])
  add_seconds=int(timeIncrement[6:8])
  add_milliseconds=int(timeIncrement[9:])
  date_new=datetime.timedelta(hours=add_hours,minutes=add_minutes,seconds=add_seconds,milliseconds=add_milliseconds)
​
  for num, i in enumerate(re.finditer(match,subtitles)):
      start=i.start()
      hours=int(subtitles[start:start+2])
      minutes=int(subtitles[start+3:start+5])
      seconds=int(subtitles[start+6:start+8])
      milliseconds=int(subtitles[start+9:start+12])
      date_old=datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds,milliseconds=milliseconds)
      final_time="0"+str(date_old+date_new)[:-3].replace(".",",")
      subtitles=subtitles.replace(subtitles[start:start+12],final_time)
    
  return subtitles

