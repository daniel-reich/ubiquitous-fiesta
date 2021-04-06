
def ave_spd(up_time, up_spd, down_spd):
  distance_total = up_time*up_spd*2
  time_total = up_time+up_time*up_spd/down_spd
  return distance_total/time_total

