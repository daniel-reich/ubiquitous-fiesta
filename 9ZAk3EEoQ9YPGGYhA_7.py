
def items_purchase(store, wallet):
  for i in store:
    store[i] = int(''.join([j for j in store[i] if j.isdigit()]))
  ret = sorted([i for i in store if store[i]<=int(wallet[1:])])
  return ret if ret else 'Nothing'

