
def lcm_three(num):
  m = max(num)
  while True:
    if m%num[0] == 0 and m%num[1] == 0 and m%num[2] == 0:
      return m
    else:
      m+=1

