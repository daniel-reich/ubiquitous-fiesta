
def get_products(lst):
​
  res = []
​
  for i in range(len(lst)):
    product = 1
    for j in range(len(lst)):
      if i != j: product *= lst[j]
​
    res.append(product)
​
  return res

