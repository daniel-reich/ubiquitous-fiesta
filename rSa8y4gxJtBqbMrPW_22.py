
def lcm(n1, n2):
  return min({n1*i for i in range(1,max(n1,n2)+1)} & {n2*i for i in range(1,max(n1,n2)+1)})

