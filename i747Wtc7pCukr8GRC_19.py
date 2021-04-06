
def products(lst):
  products = []
  for i in range(0,len(lst)-2):
    for j in range(i+1,len(lst)-1):
      for k in range(j+1,len(lst)):
        products.append(lst[i] * lst[j] * lst[k])
  return products
​
def max_product(lst):
  return max(products(lst))
  
def min_product(lst):
  return min(products(lst))

