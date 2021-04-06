
def doubled_pay(n):
  z = 1
  for x in range(1, n + 1):
    if x == 1:
      y = 1
    else:
      y *= 2
      z += y
  return z

