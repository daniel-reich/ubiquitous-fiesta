
def lcm_three(num):
  m = max(num)
  lcm = 0
  wee = 0
  while lcm == 0:
    wee += m
    if wee % num[0] == 0 and wee % num[1] == 0 and wee % num[2] == 0:
      lcm = wee
  return lcm

