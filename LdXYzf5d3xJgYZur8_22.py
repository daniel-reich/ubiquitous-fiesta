
def longest_time(h, m, s):
  m *= 60
  h *= 3600
  
  if s > m and s > h:
    return s
  elif m > s and m > h:
    return m // 60
  elif h > s and h > m:
    return h // 3600

