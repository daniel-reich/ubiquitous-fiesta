
def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def fat_prime(a, b):
  return [x for x in range(min(a,b), max(a,b)+1) if is_prime(x)][-1]

