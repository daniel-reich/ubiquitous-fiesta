
def time_saved(s_lim, s_avg, d):
  slow = (60/s_lim) * d
  fast = (60/s_avg) * d
  return round((slow - fast),1)

