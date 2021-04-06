
def alternate_sort(lst):
  
  Letters = []
  Numbers = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Type = type(lst[Counter])
    
    if (Type == int):
      Numbers.append(lst[Counter])
      Counter += 1
    
    elif (Type == str):
      Letters.append(lst[Counter])
      Counter += 1
    
    else:
      Counter += 1
  
  Numbers = sorted(Numbers)
  Letters = sorted(Letters)
  
  Combined = []
  Counter = 0
  Length = len(Letters)
  
  while (Counter < Length):
    Combined.append(Numbers[Counter])
    Combined.append(Letters[Counter])
    Counter += 1
  
  return Combined

