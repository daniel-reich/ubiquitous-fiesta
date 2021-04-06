
def happy(n):
  h = True
  s = n
  l = 0
  while s != 1:
    l = s
    s = 0
    for x in str(l):
      s += int(x)**2
    if s > l*2:
      s = 1
      h = False
  return h

