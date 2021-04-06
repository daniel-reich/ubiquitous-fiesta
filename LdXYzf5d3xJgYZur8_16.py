
def longest_time(h, m, s):
  if h*60>m and h*60*60>s:
    return h
  elif m>h*60 and m*60>s:
    return m
  else:
    return s

