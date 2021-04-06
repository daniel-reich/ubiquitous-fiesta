
def next_prime(num):
  cond = 2**(num-1) % num == 1
  if cond:
    return num
  else:
    while(not cond):
      num += 1
      cond = 2**(num-1) % num == 1
    return num

