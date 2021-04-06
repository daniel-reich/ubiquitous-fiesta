
def track_robot(*steps):
​
  Paces = []
  
  for arg in steps:
    Paces.append(arg)
  
  if (Paces == []):
    return [0, 0]
  
  Horizontal = 0
  Vertical = 0
  
  Counter = 0
  Length = len(Paces)
  
  while (Counter < Length):
    
    Item = Paces[Counter]
    
    if (Counter % 4 == 0):
      Vertical += Item
      Counter += 1
    elif (Counter % 4 == 1):
      Horizontal += Item
      Counter += 1
    elif (Counter % 4 == 2):
      Vertical -= Item
      Counter += 1
    elif (Counter % 4 == 3):
      Horizontal -= Item
      Counter += 1
    else:
      Counter += 1
  
  Answer = []
  Answer.append(Horizontal)
  Answer.append(Vertical)
  
  return Answer

