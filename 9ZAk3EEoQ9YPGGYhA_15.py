
def items_purchase(store, wallet):
  d={}
  for k, v in store.items():
    d[k]=int(v[1:].replace(',',''))
  w=int(wallet[1:])
  A=[]
  for x in d:
    if d[x]<=w:
      A.append(x)
  if A:   
    return sorted(A)
  return 'Nothing'

