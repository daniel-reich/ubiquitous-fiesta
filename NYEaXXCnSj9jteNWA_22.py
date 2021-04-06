
def ave_spd(up_time, up_spd, down_spd):
  avg_speed = (( up_spd // up_time  ) + down_spd ) / 2
  return round(avg_speed)

