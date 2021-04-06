
def legendre(p, n):
  count = 0
  i = 1
  while (p ** i) <= n:
    count += int(n / (p ** i))
    i += 1
  return count

