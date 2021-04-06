
def goldbach_conjecture(n):
  if n == 1 or n % 2:
    return []
  
  primes = [i for i in range(2,n) if is_prime(i)]
  for i in primes:
    for j in primes[::-1]:
      if i + j == n:
        return [i,j]
​
​
def is_prime(num):
  return all(num%i for i in range(2, int(num**0.5)+1))

