
def lcm(a, b):
  return min([n if n%a == 0 and n%b == 0 else a*b for n in range(1,a*b)])

