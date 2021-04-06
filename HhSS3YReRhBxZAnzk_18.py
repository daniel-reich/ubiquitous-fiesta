
def gen_values(n, i): #w/o built-in
  l = []
  if i // 1 == i:
    s = 0
    while s <= n:
      l += [s]
      s += i
  else:
    s = 0.0
    while s <= n:
      l += [s * 10001 // 100 / 100]
      s += i
  x = s * 10001 // 100 / 100
  if x == n:
      return l + [x]
  return l

