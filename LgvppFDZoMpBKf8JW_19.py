
def digital_clock(seconds):
  seconds  %= 86400
  h = seconds // 3600
  m = seconds % 3600 // 60
  s = (seconds % 3600) % 60
  
  return '{:0>2d}:{:0>2d}:{:0>2d}'.format(h,m,s)

