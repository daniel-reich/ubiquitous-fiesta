
def longest_time(h, m, s):
  d = {h:h*60*60,m:m*60,s:s}
  return max(d, key=d.get)

