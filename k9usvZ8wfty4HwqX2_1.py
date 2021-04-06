
def cuban_prime(n):
  return '{} is {}cuban prime'.format(n, '' if isprime(n) and ishex(n) else 'not ')
  
isprime = lambda n: all(n%i for i in range(2,n))
​
def ishex(n):
  a = int(((n-1)//3)**.5)
  return n == 3*a**2 + 3*a +1

