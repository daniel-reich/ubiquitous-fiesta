
def zero_indices(lst, k):
  z = [-1]+[i for i,n in enumerate(lst) if n == 0]+[len(lst)]
  m,j = 0,k+1
  for i in range(len(z)-j):
    if z[i+j]-z[i] > m:
      m = z[i+j]-z[i]
      res = z[i+1:i+j]
  return res

