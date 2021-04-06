
def c_fuge(n,k):
  factors = [i for i in range (2,n+1) if n%i==0]
  def sum_of_factors(x):
    if x in factors or x==0 or (x > 1 and any(sum_of_factors(x-i) for i in factors)):
      return True
    return False
  return sum_of_factors(k) and sum_of_factors(n-k)

