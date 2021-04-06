
def is_powerful(n):
  factors = [i for i in range(2,n) if not n % i]
  prime_factors = [i for i in factors if all([i % j for j in range(2,i)])]
  power = [i for i in prime_factors if not n % (i**2)]
  return power == prime_factors

