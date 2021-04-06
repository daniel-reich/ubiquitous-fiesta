
def moran(n):
  s = sum(map(int, str(n)))
  return 'M' if n%s==0 and n/s==n//s and all([(n//s)%i for i in range(2, (n//s)//2)]) else 'H' if n%s==0 else 'Neither'

