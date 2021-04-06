
def shuffle_count(n):
  for i in range(1,n):
    if 2**i%(n-1)==1:return i
  return 1

