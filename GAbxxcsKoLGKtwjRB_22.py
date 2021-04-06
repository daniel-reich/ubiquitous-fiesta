
primes = [i for i in range(2, 102) if all([i % j != 0 for j in range(2,i)])]
​
def sum_primes(lst):
  return sum([i for i in lst if i in primes]) or None

