
def is_unfair_hurdle(hurdles):
  
  Height = len(hurdles)
  
  if (Height >= 4):
    return True
  
  Positions = []
  Span = hurdles[0]
  
  Counter = 0
  Length = len(Span)
  
  while (Counter < Length):
    
    Item = Span[Counter]
    
    if (Item == "#"):
      Positions.append(Counter)
      Counter += 1
    else:
      Counter += 1 
  
  Previous = 0
  Current = 1
  Length = len(Positions)
  
  while (Current < Length):
    Item_A = int(Positions[Previous])
    Item_B = int(Positions[Current])
    Distance = Item_B - Item_A
    
    if (Distance < 4):
      return True
    else:
      Previous += 1
      Current += 1
  
  return False

