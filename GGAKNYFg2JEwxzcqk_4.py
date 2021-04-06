
def anti_divisors(n):
  return [i for i in range(2,n) if n%i and 0 in [j%i for j in range(2*n-1,2*n+2)]]

