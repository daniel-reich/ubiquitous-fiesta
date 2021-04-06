
def divisible(n):
  return (n**.5)%1 == 0 and is_prime(int(n**.5))
​
is_prime = lambda n: n>1 and all(n%i for i in range(2,1+int(n**.5)))

