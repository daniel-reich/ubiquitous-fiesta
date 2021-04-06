
def two_product(lst, n):
  lst1 = lst
  lst2 = lst
  l = []
  for i in lst:
    for j in lst:
      l.append([i,j])
​
  x = sorted([i for i in l if i[0] * i[1] == n]) 
  if len(x) == 0:
    return None
  return x[0]

