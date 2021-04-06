
def is_triplet(n1, n2, n3):
  n = max(n1,n2,n3)
  sum = n1*n1 + n2*n2 + n3*n3 - n*n
  return sum==n*n

