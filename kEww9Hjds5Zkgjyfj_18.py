
def replace_next_largest(lst):
  
  Sample = lst
  Maximum = max(Sample)
  Sorted = sorted(Sample)
  
  Revised = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    
    Item = Sample[Counter]
    
    if (Item == Maximum):
      Revised.append(-1)
      Counter += 1
    
    else:
      Cursor = 0
      Span = len(Sample)
    
      while (Cursor < Span):
        
        Item_A = Sample[Counter]
        Item_B = Sorted[Cursor]
        
        if (Item_A >= Item_B):
          Cursor += 1
        else:
          Revised.append(Item_B)
          Cursor += Span
      
      Counter += 1
  
  return Revised

