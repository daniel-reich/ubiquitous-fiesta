
def time_adjust(now, hrs, mins, sec):
  newTime = [hrs, mins, sec]
  time1= now.split(":")
  time = []
  for elem in time1:
    time.append(int(elem))
  for i in [2, 1, 0]:
    time[i] += newTime[i]
    if i ==0:
      time[i] = time[i] % 24
      continue
    if time[i] >= 60:
      time[i-1] += int(time[i] / 60)
      time[i] = time[i] % 60
  ans = "%02d:%02d:%02d" % (time[0], time[1], time[2])
  return ans

