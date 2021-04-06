
def simple_check(a, b):
  lst, sort = [a, b], []
  for x in lst:
    sort = [y for y in sort if y <= x] +\
    [x] + [y for y in sort if y > x]
  a, b = sort
  c = 0
  while a > 0:
    if not b % a:
      c += 1
    a, b = a - 1, b - 1
  return c

