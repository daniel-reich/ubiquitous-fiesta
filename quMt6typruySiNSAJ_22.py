
def shuffle_count(num):
  if num == 2:
    return 1
  
  k = 1
  while 2 ** k % (num - 1) != 1:
    k += 1
  return k

