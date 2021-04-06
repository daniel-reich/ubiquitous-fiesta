
def move_zeros(lst):
​
  Front = []
  Back = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Item = lst[Counter]
    Category = type(Item)
    
    if (Category == int) and (Item == 0):
      Back.append(Item)
      Counter += 1
    elif (Category == float) and (Item == 0):
      Back.append(Item)
      Counter += 1
    else:
      Front.append(Item)
      Counter += 1
      
  Answer = Front + Back
  return Answer

