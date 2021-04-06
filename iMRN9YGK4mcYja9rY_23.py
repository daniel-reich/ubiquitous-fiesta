
def accumulating_product(lst):
  if lst:
    r=[lst[0]]
    for i in range(1,len(lst)):
      r.append(lst[i]*r[-1])
    return r
  else:
    return []

