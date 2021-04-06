
def items_purchase(store, wallet):
  res = []
  for product, price in store.items():
    if int(price[1::].replace(',', "")) <= int(wallet[1::]):
      res.append(product)
  
  return sorted(res) if res != [] else "Nothing"

