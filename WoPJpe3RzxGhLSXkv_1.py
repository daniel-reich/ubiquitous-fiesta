
def concatenation_sum(n):
  k = len(str(n))
  return k*(n-10**(k-1)+1) + sum(9*10**(i-1)*i for i in range(1,k))

