
def digital_clock(seconds):
  hours, left = divmod(seconds, 3600)
  
  while hours >= 24:
    hours = hours - 24
  if left > 0:
    minutes, left = divmod(left, 60)
    if left > 0:
      return "{hh:02}:{mm:02}:{ss:02}".format(hh=hours, mm = minutes, ss = left)
    else:
      return "{hh:02}:{mm:02}:00".format(hh=hours, mm = minutes)
  else:
    return "{hh:02}:00:00".format(hh=hours)

