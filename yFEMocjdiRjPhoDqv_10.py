
def prime_in_range(n1, n2):
  return any(is_prime(k) for k in range(n1,n2+1))
​
is_prime = lambda n: n>1 and all(n%i for i in range(2, 1+int(n**.5)))

