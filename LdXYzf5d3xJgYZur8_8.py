
def longest_time(h, m, s):
  times = {h*3600:h, m*60:m, s:s}
  return times[max(times)]

