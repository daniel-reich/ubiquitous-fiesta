
def major_sum(l):
  y = 0
  c = 0
  b = 0
  for x in l:
    if x > 0:
      y += x
    if x < 0:
      c += abs(x)
    if x == 0:
      b += 1
  d = max(y, c, b)
  if d == c:
    return d * -1
  return d

