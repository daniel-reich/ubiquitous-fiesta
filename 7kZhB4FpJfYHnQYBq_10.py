
def lcm_three(num):
  lcm,m = max(num),max(num)
  while not all(not lcm%i for i in num):
    lcm += m
  return lcm

