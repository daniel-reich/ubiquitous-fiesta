
def two_product(arr, N):
  print(N)
  needed = []
  for i in arr:
    if N % i == 0:
      if i in needed:
        return [N/i, i]
      else:
        needed.append(N/i)
  return None

