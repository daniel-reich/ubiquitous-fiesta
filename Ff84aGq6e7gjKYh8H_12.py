
def minutes_to_seconds(time):
  mins, secs = [int(x) for x in time.split(":")]
  if secs >= 60:
    return False
  return mins * 60 + secs

