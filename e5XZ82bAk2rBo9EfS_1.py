
import datetime
​
def get_sleeptime(time):
  res = datetime.datetime.strptime(time[0], "%H:%M")
  res -= datetime.timedelta(hours=int(time[1][:2]), minutes=int(time[1][3:]))
  return res.strftime("%H:%M")
​
def bed_time(*times):
  return list(map(get_sleeptime, times))

