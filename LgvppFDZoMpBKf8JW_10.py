
def digital_clock(seconds):
  h = seconds // 3600  - 24 * (seconds // ( 3600 * 24))
  m = seconds % 3600 // 60
  s = seconds % 360 % 60
  return ":".join("0" + str(i) if len(str(i)) != 2 else str(i) for i in [h,m,s])

