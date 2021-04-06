
def ave_spd(up_time, up_spd, down_spd):
  d=(up_time/60)*up_spd
  return d*2/(up_time/60+d/down_spd)

