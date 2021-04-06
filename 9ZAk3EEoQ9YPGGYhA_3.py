
def items_purchase(store, w):
  w = int(w[1:].replace(",",""))
  return sorted(k for k,v in store.items() if int(v[1:].replace(",",""))<=w) \
    or "Nothing"

