
def smallest(n):
  from fractions import gcd
  ans = 1
  for i in range(1, n+1):
    ans = (ans*i)//gcd(ans, i)
  return ans

