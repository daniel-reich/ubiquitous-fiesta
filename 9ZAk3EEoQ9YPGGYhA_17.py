
def items_purchase(store, wallet):
  items = []
  for i in store:
    if int(store[i][1:].replace(',',''))<=int(wallet[1:].replace(',','')):
      items.append(i)
  return sorted(items) if len(items)>0 else 'Nothing'

