
def two_product(arr, N):
  return next(([N/n,n] for i,n in enumerate(arr) if N/n in arr[:i]),None)

