
def third_most_expensive(dct):
  
  # Making Two Lists of Names and Prices
  
  Things = []
  Prices = []
  
  for Key, Value in dct.items():
    Things.append(Key)
    Prices.append(Value)
  
  # Establishing If There Are Three or More Items
  
  if (len(Prices) < 3):
    return False
  
  # Establishing If There Are Three or More Prices
  
  Numbers = set(Prices)
  Numbers = list(Numbers)
  Numbers = sorted(Numbers, reverse = True)
  
  if (len(Numbers) < 3):
    Wanted = Numbers[-1]
  else:
    Wanted = Numbers[2]
  
  # Establishing Third Most Expensive Item
  
  Counter = 0
  Length = len(Prices)
  
  while (Counter < Length):
    Item = Things[Counter]
    Value = Prices[Counter]
    
    if (Value == Wanted):
      return Item
    else:
      Counter += 1

