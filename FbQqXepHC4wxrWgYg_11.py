
def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def prime_divisors(num):
  A=[x for x in range(1, num+1) if num%x==0]
  return [x for x in A if is_prime(x)]

