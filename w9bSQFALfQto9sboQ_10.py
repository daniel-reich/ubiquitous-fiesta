
def gcd(n1, n2):
  m = min(n1, n2)
  return max([x for x in range(1, m+1)], key = lambda x:(n1 % x == 0 and n2 % x == 0, x))

