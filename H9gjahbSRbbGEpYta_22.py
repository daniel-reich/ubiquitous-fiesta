
def multiply(n1, n2):
  prod = sum(n1 for i in range(abs(n2)))
  return prod if n2 > 0 else -prod

