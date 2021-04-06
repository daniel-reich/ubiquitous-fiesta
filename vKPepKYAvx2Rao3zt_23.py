
def car_timer(n):
  seconds = (n * 60) % (24 * 3600) 
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60   
  t = "%02d:%02d" % (hour, minutes) 
  return int(t[0]) + int(t[1]) + int(t[3]) + int(t[4])

