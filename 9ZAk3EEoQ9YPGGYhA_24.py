
def items_purchase(store, wallet):
  l=sorted(i for i,p in store.items() if int(p[1:].replace(",",""))<=int(wallet[1:]))
  return "Nothing" if not l else l

