
def longest_time(h, m, s):
  dict = {(h*60*60):h, (m * 60):m, s:s}
  value = sorted(dict.keys())
  return dict.get(value[-1])

