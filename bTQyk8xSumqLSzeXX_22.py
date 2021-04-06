
def has_valid_price(product):
  
  if (product == None):
    return False
  
  Numbers = []
  
  for x, y in product.items():
    if (x == "price"):
      Numbers.append(y)
  
  if (Numbers == []):
    return False
  
  Counter = 0
  Length = len(Numbers)
  
  while (Counter < Length):
    
    Item = Numbers[Counter]
    Type = type(Item)
    
    if (Type == int) and (Item >= 0):
      Counter += 1
    elif (Type == float) and (Item >= 0.0):
      Counter += 1
    else:
      return False
  
  return True

