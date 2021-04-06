
def ave_spd(up_time, up_spd, down_spd):
  down_time = (up_spd/ down_spd)*up_time 
  return up_time*up_spd/(up_time + down_time)*2

