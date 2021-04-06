
def digital_clock(ts):
  h, m, s = (ts // 3600) % 24, (ts // 60) % 60, ts % 60
  return "{:02d}:{:02d}:{:02d}".format(h, m, s)

