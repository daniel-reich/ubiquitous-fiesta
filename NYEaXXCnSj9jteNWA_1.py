
def ave_spd(up_time, up_spd, down_spd):
  up_time /= 60
  distance = up_spd * up_time
  down_time = distance / down_spd
  return (2 * distance) / (down_time + up_time)

