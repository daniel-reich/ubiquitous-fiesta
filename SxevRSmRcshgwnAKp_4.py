
def pricey_prod(d):
  return sorted([i for i in d if d[i]>499],key=lambda x:-d[x])

