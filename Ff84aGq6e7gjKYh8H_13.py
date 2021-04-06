
def minutes_to_seconds(time):
  t=time.split(':')
  if int(t[1])>=60:
    return False
  else:
    s=int(t[0])*60+int(t[1])
    return s

