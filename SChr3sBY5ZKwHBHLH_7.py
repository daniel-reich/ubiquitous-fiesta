
def sort_it(lst):
  
  Counter = 0
  Length = len(lst)
  
  Numbers = []
  Lists = []
  Values = []
  
  while (Counter < Length):
    
    Item = lst[Counter]
    Type = type(Item)
    
    if (Type == list):
      Thing = int(Item[0])
      Lists.append(Thing)
      Values.append(Thing)
      Counter += 1
    elif (Type == int):
      Numbers.append(Item)
      Values.append(Item)
      Counter += 1
    else:
      Counter += 1
  
  Values = sorted(Values)
  Answer = []
  
  Counter = 0
  Length = len(Values)
  
  while (Counter < Length):
    
    Item = Values[Counter]
    
    if (Item in Lists):
      Batch = []
      Batch.append(Item)
      Answer.append(Batch)
      Counter += 1
    elif (Item in Numbers):
      Answer.append(Item)
      Counter += 1
    else:
      Counter += 1
    
  return Answer

