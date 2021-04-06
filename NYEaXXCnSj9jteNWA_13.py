
def ave_spd(up_time, up_spd, down_spd):
  return (up_time * up_spd * 2) // (up_time + (up_time * up_spd) / down_spd)

