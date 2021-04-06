
def time_saved(s_lim, s_avg, d):
  t_1 = (d/s_lim)*60
  t_2 = (d/s_avg)*60
  return round((abs(t_2-t_1)),1)

