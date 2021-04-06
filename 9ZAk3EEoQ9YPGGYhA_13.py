
def items_purchase(store, wallet):
  store = {k:int(v.replace(',','')[1:]) for k,v in store.items()}
  res = sorted(k for k,v in store.items() if v <= int(wallet[1:]))
  return res if res else 'Nothing'

