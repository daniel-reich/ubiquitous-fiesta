
from itertools import combinations as C
def two_product(lst, n):
  A=[]
  for x in C(lst,2):
    if x[0]*x[-1]==n:
      A.append(x)
  if A:
    return sorted(A[0])
  else:
    return None

