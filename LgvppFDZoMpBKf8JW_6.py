
def digital_clock(seconds):
  hd,ms=divmod(seconds,3600)
  h=hd%24
  m,s=divmod(ms,60)
  return "{:02d}:{:02d}:{:02d}".format(h,m,s)

