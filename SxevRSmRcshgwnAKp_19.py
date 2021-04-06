
def get_key(wanted, d, chosen):
  
  for key, value in d.items():
    if wanted == value:
      chosen.append(key)  
​
def pricey_prod(d):
  
  # Extracting Items of 500+
  Names = []
  Numbers = []
  
  for x, y in d.items():
    Names.append(x)
    Numbers.append(y)
  
  Layer_One = {}  
  
  Counter = 0
  Length = len(Numbers)
  
  while (Counter < Length):
    Key = Names[Counter]
    Value = Numbers[Counter]
    
    if (Value >= 500):
      Layer_One[Key] = Value
      Counter += 1
    else:
      Counter += 1
  
  Names = []
  Numbers = []
  
  for x, y in Layer_One.items():
    Names.append(x)
    Numbers.append(y)
  
  Numbers = sorted(Numbers, reverse=True)
  
  Products = []
  
  Counter = 0
  Length = len(Numbers)
  
  while (Counter < Length):
    
    Item = Numbers[Counter]
    get_key(Item, Layer_One, Products)
    Counter += 1
  
  return Products

