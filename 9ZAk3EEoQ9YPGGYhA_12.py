
def items_purchase(store, wallet):
  store = {k:int(v.replace(',', '')[1:]) for k,v in store.items()}
  wallet, basket = int(wallet[1:]), []
  
  for i in store:
    if store[i] <= wallet:
      basket.append(i)
      
  return 'Nothing' if len(basket) == 0 else sorted(basket)

