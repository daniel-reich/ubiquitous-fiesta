
def chosen_wine(wines):
  
  if (wines == []):
    return None
  
  Amounts = []
  
  Counter = 0
  Length = len(wines)
  
  while (Counter < Length):
    Item = wines[Counter]
    Value = Item["price"]
    Amounts.append(Value)
    Counter += 1
  
  Amounts = set(Amounts)
  Amounts = list(Amounts)
  Amounts = sorted(Amounts)
  
  Span = len(Amounts)
  
  if (Span == 1):
    Wanted = Amounts[0]
  else:
    Wanted = Amounts[1]
  
  Counter = 0
  Length = len(wines)
  
  while (Counter < Length):
    Item = wines[Counter]
    Value = Item["price"]
    
    if (Value == Wanted):
      return Item["name"]
    else:
      Counter += 1

