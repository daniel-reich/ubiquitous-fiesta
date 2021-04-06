
def gcd(lst):
  return max(set.intersection(*[{i for i in range(1,n+1) if n%i==0} for n in lst]))

