
def shuffle_count(num):
  k = 1
  if num == 2:
    return 1
  while k <= num:
    if (2**k % (num-1)) == 1:
      return k
    k += 1

