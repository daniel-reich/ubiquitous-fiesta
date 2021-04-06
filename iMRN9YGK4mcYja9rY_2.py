
def accumulating_product(l):
  for i in range(1,len(l)):
    l[i] *= l[i-1]
  return l

