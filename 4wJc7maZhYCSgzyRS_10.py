
def two_product(arr, N):
  products = []
  for i in arr:
    if N % i == 0:
      if N//i in products:
        return [N//i, i]
      else:
        products.append(i)

