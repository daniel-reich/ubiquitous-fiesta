
def almost_sorted(lst):
  
  Original = lst
  
  Forward = sorted(Original)
  Backward = sorted(Original, reverse=True)
    
  if (Original == Forward) or (Original == Backward):
    return False
    
  Counter = 0
  Length = len(Original)
  
  while (Counter < Length):
        
    Exhibit = []
        
    Cursor = 0
    Span = len(Original)
        
    while (Cursor < Span):
      Item = Original[Cursor]
            
      if (Cursor == Counter):
        Cursor += 1
      else:
        Exhibit.append(Item)
        Cursor += 1
        
    Sample_A = sorted(Exhibit)
    Sample_B = sorted(Exhibit, reverse=True)
        
    if (Exhibit == Sample_A) or (Exhibit == Sample_B):
      return True
    else:
      Counter += 1
  
  return False

