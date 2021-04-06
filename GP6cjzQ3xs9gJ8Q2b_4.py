
def is_polydivisible(n):
  A=[int(str(n)[:i]) for i in range(1, len(str(n))+1)]
  return all(A[i]%(i+1)==0 for i in range(len(A)))

