
def two_product(l,n):
  for i in l:
    for j in l:
      if i*j==n: return sorted([i,j])

