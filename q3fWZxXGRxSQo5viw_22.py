
def cal(d):
  # 5 cm / h
  # it can crawl for 30 mins
  # 10 mins rest and slides down 30 cms
  s = 5
  t = 30
  r = 10
  b = 30
  a = 0
  while d >= 0:
    for i in range(t):
      if d<=0: return a
      d -= s
      a += 1
    for i in range(r):
      if d<=0: return a
      a += 1
    if d >= 0:
      d += 30
  return a

