
def bill_split(spicy, cost):
  
  Me = 0
  Friend = 0
  Shared = 0
  
  Counter = 0
  Length = len(spicy)
  
  while (Counter < Length):
    
    Content = str(spicy[Counter])
    Value = int(cost[Counter])
    
    if (Content == "S"):
      Me += Value
      Counter += 1
    else:
      Shared += Value
      Counter += 1
    
  Split = Shared / 2
  Me += Split
  Friend += Split
  
  Bill = []
  Bill.append(Me)
  Bill.append(Friend)
  
  return Bill

