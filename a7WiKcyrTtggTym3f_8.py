
def lcm(a,b):
  for i in range(1,b+1):
    if (a*i)%b==0:
      return a*i
      break

