
def bed_time(*times):
  time = []
  for i in range(len(times)):
    first_hour = get_HourMinutes(times,i , 0)[0]
    first_minutes = get_HourMinutes(times,i , 0)[1]
    second_hour = get_HourMinutes(times,i , 1)[0]
    second_minutes = get_HourMinutes(times,i , 1)[1]
    sleep_hour = (first_hour-second_hour)%24
    sleep_minutes = (first_minutes-second_minutes)%60
    if (first_minutes-second_minutes) < 0:
      sleep_hour += -1
    time_string = ""
    if sleep_hour >= 10:
      time_string = str(sleep_hour) + ":"
    else:
      time_string = "0" + str(sleep_hour) + ":"
    if sleep_minutes >= 10:
      time_string += str(sleep_minutes)
    else:
      time_string += "0" + str(sleep_minutes)
    time.append(time_string)
  return time
​
def get_HourMinutes(times, i, index_time):
  hourMinutes = []
  time = times[i]
  index = time[index_time].find(":")
  hourMinutes.append(int(time[index_time][:index]))
  hourMinutes.append(int(time[index_time][index+1:]))
  return hourMinutes

