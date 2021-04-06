
def time_saved(s_lim, s_avg, d):
  t1 = (60/s_avg) * d
  t2 = (60/s_lim) * d
  return round(t2 -t1, 1)

