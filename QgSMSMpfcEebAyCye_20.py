
def time_saved(s_lim, s_avg, d):
  #speed = distance / time
  minutes_in_hour = 60
  time_limit = d / s_lim * minutes_in_hour
  time_avg = d / s_avg * minutes_in_hour
  return round(time_limit - time_avg, 1)

