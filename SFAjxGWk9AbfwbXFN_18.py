
def primes_below_num(n):
  a = []
  for i in range(2, n+1):
    if len([j for j in range(2, i+1) if i%j==0]) <= 1:
      a.append(i)
  return a

