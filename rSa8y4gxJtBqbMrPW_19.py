
def lcm(n1, n2):
  def gcd(a, b):
    if b == 0:
      return a
    return gcd(b, a % b)
  return int((n1 * n2) / gcd(n1, n2))

