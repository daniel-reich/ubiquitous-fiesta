
def max_product(n):
  max_prod = max(product(i) for i in range(1,n+1))
  return [i for i in range(1,n+1) if product(i)==max_prod]
​
​
​
​
def product(n):
  p = 1
  for i in str(n):
    p*=int(i)
  return p

