
def multiply(n1, n2):
  if n2<0:
    return -sum(n1 for i in range(abs(n2)))
  return sum(n1 for i in range(n2))

