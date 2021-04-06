
def primes_below_num(n):
  return [i for i in range(2,n+1) if all(i%j for j in range(2,i))]

