
def items_purchase(store, wallet):
  x = []
  keys = list(store.keys())
  vals = list(store.values())
  for i in store:
      if float(store[i].strip('$').replace(',', '')) <= float(wallet.strip('$').replace(',', '')):
        x.append(keys[keys.index(i)])
  if len(x) == 0:
    return 'Nothing'
  else: return sorted(x)

