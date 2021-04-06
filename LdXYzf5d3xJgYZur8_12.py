
def longest_time(h, m, s):
  #convert all to seconds
  h2s = h * 3600
  m2s = m * 60
  if max(h2s,m2s,s) == h2s:
    return h
  elif max(h2s,m2s,s) == m2s:
    return m
  return s

