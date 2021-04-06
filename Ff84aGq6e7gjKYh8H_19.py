
def minutes_to_seconds(time):
  sec = int(time[-2:])
  if sec < 60:
    return int(time[:-3]) * 60 + sec
  else:
    return False

