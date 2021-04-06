
def max_product(n):
  largest_product = [0]
  max_product = 0
  for x in range(n+1):
    digits = x
    current_product = 1
    while digits > 0:
      current_product *= (digits%10)
      digits //= 10
    if current_product == max_product:
      largest_product.append(x)
    elif current_product > max_product:
      largest_product = [x]
      max_product = current_product
  return largest_product

