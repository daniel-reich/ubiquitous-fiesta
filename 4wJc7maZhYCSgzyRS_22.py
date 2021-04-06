
def two_product(arr, N):
  a = []
  for x in arr:
    for y in a:
      if x * y == N:
        return [y, x]
    if N % x == 0:
      a.append(x)

