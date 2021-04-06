
def gcd(lst):
  factors = [i for i in range(1,min(lst)+1) if all(j%i==0 for j in lst)]
  return max(factors)

