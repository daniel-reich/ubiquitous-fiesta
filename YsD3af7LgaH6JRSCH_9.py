
def time_adjust(now, hrs, mins, sec):
  hour, min, second = now.split(':')
  min_add = (int(second) + sec)//60
  s = (int(second) + sec)%60
  if min_add:
    mins += min_add
  hour_add = (int(min) + mins)//60
  m = (int(min) + mins)%60
  if hour_add:
    hrs += hour_add
  h = (int(hour) + hrs)%24
  return "{:02}:{:02}:{:02}".format(h, m, s)

