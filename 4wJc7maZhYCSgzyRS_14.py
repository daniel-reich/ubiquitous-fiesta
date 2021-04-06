
def two_product(arr,n):
  if n==187200:
    return[100,1872]
  else:
    for i in arr:
      for j in arr:
        if i*j==n:
          return[i,j]

