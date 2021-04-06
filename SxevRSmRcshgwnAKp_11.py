
def pricey_prod(d):
  return sorted([i[0] for i in d.items() if i[1]>=500],key=lambda x:d[x])[::-1]

