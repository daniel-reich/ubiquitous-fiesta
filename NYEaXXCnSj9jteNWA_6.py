
def ave_spd(up_time, up_spd, down_spd):
  s = up_time * up_spd
  t = s // down_spd
  return s // (up_time - t)

