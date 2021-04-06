
def longest_time(h, m, s):
  time_dict = {h: h * 3600, m: m * 60, s: s}
  return max(time_dict, key = time_dict.get)

