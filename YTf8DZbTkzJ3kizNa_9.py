
import gmpy2
def moran(n):
  h=sum(int(i) for i in str(n))
  return 'M' if gmpy2.is_prime(int(n/h)) else 'H' if n%h==0 else 'Neither'

