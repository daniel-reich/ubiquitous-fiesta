
def time_saved(s_lim, s_avg, d):
  a = d/s_lim
  b = d/s_avg
  return round((a-b)*60,1)

