
def minutes_to_seconds(time):
  m,s = time.split(":")
  if int(s) >= 60: return False
  return int(m)*60 + int(s)

