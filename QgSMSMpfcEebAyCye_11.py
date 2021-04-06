
def time_saved(s_lim, s_avg, d):
  fast_time = d/s_avg * 60
  slow_time = d/s_lim * 60
  return round(slow_time - fast_time, 1)

