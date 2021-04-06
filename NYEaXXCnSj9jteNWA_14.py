
def ave_spd(up_time, up_spd, down_spd):
  d = up_spd*up_time/60
  down_time = d/down_spd
  return round(2 * d /( (up_time/60) + down_time), 0)

