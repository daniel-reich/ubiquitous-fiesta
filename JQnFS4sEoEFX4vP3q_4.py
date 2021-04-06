
def product_pair(lst, k):
  from itertools import permutations as p
  def products(lst):
    ps = []
    for l in lst:
      product = 1
      for int in l:
        product *= int
      ps.append(product)
    return ps
  
  p = [list(i) for i in list(p(lst,k))]
  ps = products(p)
  
  try:
    return min(ps), max(ps)
  except:
    return None

