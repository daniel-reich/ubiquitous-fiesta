
def lcm(a,b):
  return min(i for i in range(1,a*b+1) if i%a==0 and i%b==0)

