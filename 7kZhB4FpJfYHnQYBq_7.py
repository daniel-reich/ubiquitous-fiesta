
def lcm_three(num):
  from fractions import gcd
  lcm = num[0]
  for i in num[1:]:
    lcm = lcm*i/gcd(lcm, i)
  return int(lcm)

