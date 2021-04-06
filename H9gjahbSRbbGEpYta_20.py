
def multiply(n1, n2):
  sign = lambda x: (x>0) - (x<0)
  v = sum(abs(n1) for _ in range(abs(n2)))
  return v if sign(n1)==sign(n2) else -v

