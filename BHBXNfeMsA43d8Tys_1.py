
def pi(n):
  Pi = 0
  iter = 3*(10**(n+10))//8
  for i in range(1,2*n):
    Pi+= iter//(2*i+1)
    iter = iter*(2*i+1)//(8*i+8)
    
  return "3." + str(Pi)[:n]

