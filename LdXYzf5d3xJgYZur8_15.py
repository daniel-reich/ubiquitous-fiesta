
def longest_time(h, m, s):
  durations = {
  h: 3600 * h, 
  m: 60 * m, 
  s: s
  }
  for key, value in durations.items():
    if value == max(durations.values()):
      return key

