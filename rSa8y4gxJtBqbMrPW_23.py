
def lcm(n1, n2):
  return max(n1, n2) if max(n1, n2) % min(n1, n2) == 0 else n1*n2

