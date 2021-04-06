
def trailing_zeros(n):
  count=0
  for i in range(1,n):
    if n//(5**i)>=1:count+=n//(5**i)
    else:return count
  return count

