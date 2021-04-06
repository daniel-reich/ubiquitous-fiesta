
def doubleton(n):
  n, c = n + 1, 0
  while c < 1:
    x, y, lst = n, 0, []
    while x:
      if x % 10 not in lst:
        lst += [x % 10]
        y += 1
      x //= 10
    if y == 2:
      c += 1
    else:
      n += 1
  return n

