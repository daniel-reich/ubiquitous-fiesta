
def max_product(n):
  out = []
  highest = 0
  for i in range(n+1):
    product = 1
    for j in str(i):
      product *= int(j)
    if product>highest:
      out = [int(i)]
      highest = product
    elif product == highest:
      out.append(int(i))
  return out

