
def two_product(arr, N):
  div = []
  for n in arr:
    if N % n == 0:
      if N / n in div:
        return [N / n, n]
      div.append(n)
  return None

