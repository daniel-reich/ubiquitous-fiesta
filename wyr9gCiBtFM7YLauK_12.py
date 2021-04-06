
import datetime
​
def time_sum(times):
  if times == []:
    return [0, 0, 0]
  hours = []
  mins = []
  secs = []
  for time in times:
    clock = time.split(":")
    hours.append(int(clock[0]))
    mins.append(int(clock[1]))
    secs.append(int(clock[2]))
  hours_pre = sum(hours)
  mins_hours = str(datetime.timedelta(minutes = sum(mins))).split(":")
  secs_mins = str(datetime.timedelta(seconds = sum(secs))).split(":")
  final_hours = hours_pre + int(mins_hours[0]) + int(secs_mins[0])
  final_mins = int(mins_hours[1]) + int(secs_mins[1])
  final_secs = int(mins_hours[2]) + int(secs_mins[2])
  return [final_hours, final_mins, final_secs]

