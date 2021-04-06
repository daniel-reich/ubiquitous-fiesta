
def time_saved(s_lim, s_avg, d):
  tim1 = (d/s_lim)*60
  tim2 = (d/s_avg)*60
  return round(tim1 - tim2,1)

