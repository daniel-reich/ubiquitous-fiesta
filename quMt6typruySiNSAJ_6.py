
def shuffle_count(num):
  sol = 1
  for i in range(1,num):
    if 2**i % (num-1) == 1:
      sol = i
      break
  return sol

