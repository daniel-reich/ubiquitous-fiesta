
def minutes_to_seconds(time):
  if int(time.split(":")[1]) >= 60:
    return False
  return int(time.split(":")[0])*60 + int(time.split(":")[1])

