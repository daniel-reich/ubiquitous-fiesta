
def price_importance_sort(dct, b):
  A=sorted(dct, key=lambda x: dct[x]["price"]/dct[x]["importance"])
  B=[]
  c=0
  for x in A:
    if c+dct[x]['price']<=b:
      B.append(x)
      c+=dct[x]['price']
    else:
      break
  return sorted(B)

