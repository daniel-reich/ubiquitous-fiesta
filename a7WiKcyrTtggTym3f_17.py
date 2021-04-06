
def lcm(a, b):
  return min([b*j for j in range(1,a+1) if b*j in [a*i for i in range(1,b+1)]])

