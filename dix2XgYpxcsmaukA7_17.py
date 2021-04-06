
def express_factors(n):
  factors = []
  ret = ''
  for i in range(2,n+1):
    while not n%i:
      factors.append(i)
      n /= i
  for j in sorted(set(factors)):
    if factors.count(j) > 1: ret+=(str(j)+'^'+str(factors.count(j))+' x ')
    else: ret+=(str(j)+' x ')
    
  return ret.strip(' x')

