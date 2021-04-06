
def pentagonal(num):
  if num==1: return 1
  return pentagonal(num-1) + 5*(num-1)

