
def intersection(h1, h2):
  
  Selection = []
  
  for x in h1.keys():
    Selection.append(x)
  
  for y in h2.keys():
    Selection.append(y)
    
  Wanted = []
  
  Counter = 0
  Length = len(Selection)
  
  while (Counter < Length):
  
    Item = Selection[Counter]
    Events = Selection.count(Item)
    
    if (Events > 1) and (Item not in Wanted):
      Wanted.append(Item)
      Counter += 1
    else:
      Counter += 1
  
  First = {}
  Second = {}
  
  for key,value in h1.items():
    if (key in Wanted):
      First[key] = value
  
  for key,value in h2.items():
    if (key in Wanted):
      Second[key] = value
      
  Answer = []
  Answer.append(First)
  Answer.append(Second)
  
  return Answer

