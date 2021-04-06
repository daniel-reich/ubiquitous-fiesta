
def pricey_prod(d):
  return [i[0] for i in sorted([[k,v] for k,v in d.items() if v>499], key=lambda x:x[1], reverse=True)]

