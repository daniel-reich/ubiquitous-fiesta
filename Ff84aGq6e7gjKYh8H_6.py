
def minutes_to_seconds(time):
  if int(time[-2:]) >= 60:
    return False
  else:
    return int(time[:time.index(':')]) * 60 + int(time[-2:])

