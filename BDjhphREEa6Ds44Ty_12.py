
def line_intersect(l1, l2):
  m1, b1 = l1
  m2, b2 = l2
  x = (b2 - b1) / (m1 - m2)
  return (round(x), round(m1 * x + b1))
​
def circles_intersect(c1, c2):
  x1, y1, r1 = c1
  x2, y2, r2 = c2
  dy = (y2 - y1) or 0.000001
  return ((x1 - x2)/dy, (r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2) / (2 * dy))
​
def bomb(lst):
  if lst[0][2] == 0: return (lst[0][0], lst[0][1])
  if lst[1][2] == 0: return (lst[1][0], lst[1][1])
  if lst[2][2] == 0: return (lst[2][0], lst[2][1])
  for s in lst:
      s[2] *= 0.343
  return line_intersect(circles_intersect(lst[0], lst[1]), circles_intersect(lst[0], lst[2]))

