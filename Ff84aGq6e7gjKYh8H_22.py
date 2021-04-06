
def minutes_to_seconds(time):
  lst  = time.split(':')
  if int(lst[1]) < 60:
    return ((int(lst[0]) * 60) +( int(lst[1])))
  else:
    return False

