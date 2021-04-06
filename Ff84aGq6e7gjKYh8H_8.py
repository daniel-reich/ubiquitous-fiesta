
def minutes_to_seconds(time):
  t = time.split(":")
  return int(t[0])*60+int(t[-1]) if int(t[-1]) < 60 else False

