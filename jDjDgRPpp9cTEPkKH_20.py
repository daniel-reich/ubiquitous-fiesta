
def over_time(a):
  s, e, p, o = a
  d = 0
  if s % 1 > 0:
    d = p * (1 - s % 1)
    s = s // 1 + 1
  while s < e:
    if s < 17:
      d += p
    else:
      d += p * o
    s += 1
  # bypass python rounding #
  if d * 1000 % 10 >= 5:
    d = (d * 100 + 1) / 100
  return '${0:.2f}'.format(d)

