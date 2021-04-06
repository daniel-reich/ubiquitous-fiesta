
def product_of_primes(num):
  return len([i for i in range(2,1+int(num**.5)) if num%i==0]) == 1

