
def prime_numbers(n):
  return len([x for x in range(n) if is_prime(x)])
​
def is_prime(n):
  return n > 1 and all(n%x for x in range(2, int(n**.5)+1))

