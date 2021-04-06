
def only_5_and_3(n):
  if n % 5 == 0:
    return True
  t = 3
  while t <= n:
    if (n - t) % 5 == 0:
      return True
    t *= 3
  return False

