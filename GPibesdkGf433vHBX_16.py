
def is_prime(n):
  return n>1 and all(n%i for i in range(2,int(n**.5)+1))
def goldbach_conjecture(n):
  for i in range(n):
    for j in range(n):
      if is_prime(i) and is_prime(j) and i+j==n:
        return [i, j]

