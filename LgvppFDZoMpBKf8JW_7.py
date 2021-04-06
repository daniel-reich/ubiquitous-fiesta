
def digital_clock(seconds):
  hours = 0
  minutes = 0
  seconds2 = 0
  while seconds != 0:
    if seconds >= 86400:
      seconds -= 86400
    elif seconds > 3600:
      seconds -= 3600
      hours += 1
    elif seconds >= 60:
      seconds -= 60
      minutes += 1
    else:
      seconds2 += seconds
      seconds -= seconds
  return '{:02}:{:02}:{:02}'.format(hours,minutes,seconds2)

