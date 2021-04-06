
def diving_minigame(lst):
​
  Meter_Reading = 10
​
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Item = lst[Counter]
    
    if (Item < 0):
      Meter_Reading -= 2
    else:
      Meter_Reading += 4
      
    if (Meter_Reading > 10):
      Meter_Reading = 10
      Counter += 1
    elif (Meter_Reading <= 0):
      return False
    else:
      Counter += 1
      
  return True

