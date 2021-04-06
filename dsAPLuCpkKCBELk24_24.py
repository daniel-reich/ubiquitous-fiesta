
def get_products(lst):
  final = []
  product = 1
  for i in range(0,len(lst)):
    for j in range(0,len(lst)):
      if j == i:
        product*=1
      else:
        product*=lst[j]
    final.append(product)
    product = 1
  return final

