
def lcm(nums):
  from fractions import gcd
  l = 1
  for i in nums:l=l*i/gcd(l,i)
  return l

