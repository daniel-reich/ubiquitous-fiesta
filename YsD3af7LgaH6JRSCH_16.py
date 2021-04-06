
def time_adjust(now, hrs, mins, sec):
  time1 = now.split(':')
  time2 = [hrs, mins, sec]
  for i in range(3):
    time1[i] = int(time1[i]) + time2[i]
  time1[0] = (time1[0] + (time1[2] // 60 + time1[1]) // 60) % 24
  time1[1] = (time1[2] // 60 + time1[1]) % 60
  time1[2] = time1[2] % 60
  for i in range(3):
    time1[i] = str(time1[i])
    if len(time1[i]) == 1:
      time1[i] = '0' + time1[i]
  return ':'.join(time1)

