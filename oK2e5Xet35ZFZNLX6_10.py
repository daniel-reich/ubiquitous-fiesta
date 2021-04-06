
def neighboring(txt):
  
  Code = "abcdefghijklmnopqrstuvwxyz"
  
  First = 0
  Second = 1
  Length = len(txt)
  
  while (Second < Length):
    
    Item_A = txt[First]
    Item_B = txt[Second]
    
    Place_A = Code.index(Item_A)
    Place_B = Code.index(Item_B)
    
    Span = abs(Place_A - Place_B)
    
    if (Span == 1):
      First += 1
      Second += 1
    else:
      return False
      
  return True

