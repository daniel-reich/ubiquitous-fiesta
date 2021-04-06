
def minutes_to_seconds(time):
  a,b = time.split(":")
  if int(b)>59:
    return False
  return int(a)*60 + int(b)

