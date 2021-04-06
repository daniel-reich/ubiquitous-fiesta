
def lcm(n1, n2):
  for i in range(2,min(n1,n2)+1):
    if(n1%i==0 and n2%i==0):
      return i*lcm(int(n1/i),int(n2/i))       
  return n1*n2

