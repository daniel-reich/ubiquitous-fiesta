
def ave_spd(up_time, up_spd, down_spd):
  distance = (up_time/60) * up_spd
  down_time = distance/down_spd
  average_speed=(distance*2)/(down_time+up_time/60)
  return average_speed

