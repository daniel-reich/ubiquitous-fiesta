
def items_purchase(store, wallet):
  
  Products = []
  Prices = []
  
  for key, value in store.items():
    Products.append(key)
    Prices.append(value)
  
  Counter = 0
  Length = len(Prices)
  
  while (Counter < Length):
    Item = Prices[Counter]
    Tweak1 = Item.replace("$","")
    Tweak2 = Tweak1.replace(",","")
    Revised = Tweak2
    Prices[Counter] = Revised
    Counter += 1
  
  Available = wallet.replace("$","")
  Available = Available.replace(",","")
  Can_Buy = []
  
  Counter = 0
  Length = len(Prices)
  
  while (Counter < Length):
    Available = int(Available)
    Needed = int(Prices[Counter])
    
    if (Available >= Needed):
      Can_Buy.append(Products[Counter])
      Counter += 1
    else:
      Counter += 1
  
  Answer = sorted(Can_Buy)
  
  if (Answer == []):
    return "Nothing"
  else:
    return Answer

