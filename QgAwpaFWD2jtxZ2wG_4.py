
def sum_digits(n):
  if n==0:
    return 1
  k = 0
  j = n
  while (int(j)>0):
    k += 1
    j /= 10
  return k

