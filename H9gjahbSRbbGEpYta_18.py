
def multiply(n1, n2):
  res = 0
  for _ in range(abs(n2)):
    res += n1
  return -res if n2<0 else res

