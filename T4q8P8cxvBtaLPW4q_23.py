
def extract_primes(n):                        # Find all prime numbers in decimal integer
  is_prime = lambda n: all(n%i for i in range(2, int(n**0.5)+1)) if n>2 and n%2 else n==2
  prime_list, num = [], 2
  while num <= n:
    if is_prime(num):
      if str(num) in str(n): prime_list += [num] * str(n).count(str(num))
    num += 1
  return prime_list

