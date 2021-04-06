
def moran(n):
  s = sum(int(x) for x in str(n))
  return 'M' if is_prime (int(n/s)) and n>1 else 'H' if  n % s == 0 else 'Neither'
  
def is_prime(x):
  return all(x%i != 0 for i in range(2,x))

