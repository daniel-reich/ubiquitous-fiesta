
def flatten(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append([])
    
  Draft_One = Parameters[0]
  Draft_Two = Parameters[1]
  
  Embedded = 0
  Counter = 0
  Length = len(Draft_One)
  
  while (Counter < Length):
    Item = Draft_One[Counter]
    Category = type(Item)
    
    if (Category == list):
      Draft_Two.extend(Item)
      Embedded += 1
      Counter += 1
    else:
      Draft_Two.append(Item)
      Counter += 1
  
  if (Embedded == 0):
    return Draft_Two
  else:
    Draft_One = Draft_Two
    Draft_Two = []
    return flatten(Draft_One, Draft_Two)

