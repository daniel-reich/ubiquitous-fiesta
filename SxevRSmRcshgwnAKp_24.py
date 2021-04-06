
def pricey_prod(d):
  lst = [i for i in d if d[i] >= 500]
  return sorted(lst, key=lambda x: d[x], reverse=True)

