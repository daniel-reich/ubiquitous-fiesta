
def longest_time(h, m, s):
  m = {h*60*60:h, m*60:m, s:s}
  return m[max(m)]

