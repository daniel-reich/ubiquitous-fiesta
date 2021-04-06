
def lcm(nums):
  from fractions import gcd
  lcm = nums[0]
  for i in nums[1:]:
    lcm = lcm*i/gcd(lcm, i)
  return lcm

