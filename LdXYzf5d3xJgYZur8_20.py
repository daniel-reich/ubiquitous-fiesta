
def longest_time(h, m, s):
  t = max([h * 3600, m * 60, s]) 
  if t == h * 3600:
    return h
  elif t == m * 60:
    return m
  else:
    return s

