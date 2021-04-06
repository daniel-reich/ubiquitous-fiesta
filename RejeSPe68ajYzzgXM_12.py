
def combine(lst):
  
  Details = lst
  Details = sorted(Details)
  
  Draft_One = {}
    
  Batch = []
  Counter = 0
  Length = len(Details)
    
  while (Counter < Length):
        
    Item = Details[Counter]
        
    if (Batch == []):
      Batch.extend(Item)
      Counter += 1
        
    elif (Item[0] == Batch[0]):
      Batch.extend(Item)
      Counter += 1
        
    else:
      Draft_One[Batch[0]] = Batch
      Batch = Item
      Counter += 1
​
  Draft_One[Batch[0]] = Batch
​
  Draft_Two_Keys = []
  Draft_Two_Values = []
    
  for x,y in Draft_One.items():
    Draft_Two_Keys.append(x)
    Draft_Two_Values.append(y)
​
  Counter = 0
  Length = len(Draft_Two_Values)
    
  while (Counter < Length):
        
    Item = Draft_Two_Values[Counter]
    First = Item[2]
    Second = Item[5]
    Revised = []
    Revised.append(First)
    Revised.append(Second)
    Draft_Two_Values[Counter] = Revised
    Counter += 1
        
  Dictionary = {}
    
  Counter = 0
  Length = len(Draft_Two_Values)
    
  while (Counter < Length):
    Key = Draft_Two_Keys[Counter]
    Value = Draft_Two_Values[Counter]
    Dictionary[Key] = Value
    Counter += 1
    
  return Dictionary

