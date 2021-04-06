
def lcm(n1, n2):
  maxx = max(n1, n2)
  return maxx if maxx%n1==0 and maxx%n2==0 else n1*n2

