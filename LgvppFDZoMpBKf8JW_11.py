
def digital_clock(seconds):
  h, rs = divmod(seconds, 3600)
  return '{:02}:{:02}:{:02}'.format(h%24, rs//60, rs%60)

