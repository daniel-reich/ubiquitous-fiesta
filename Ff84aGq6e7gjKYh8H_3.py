
def minutes_to_seconds(time):
  a = time.split(':')[0]
  b = time.split(':')[1]
  c = int(a)*60 + int(b)
  if (int(b)>=60) :
    return False
  else :
    return c

