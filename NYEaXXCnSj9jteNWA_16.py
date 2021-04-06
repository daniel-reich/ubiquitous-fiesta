
def ave_spd(up_time, up_spd, down_spd):
  d = up_time * (up_spd/60)
  down_time = d / (down_spd/60)
  return 2 * d * 60 / (up_time + down_time)

