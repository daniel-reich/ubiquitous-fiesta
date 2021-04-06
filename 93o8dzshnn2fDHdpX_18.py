
def lst_ele_sum(Original):
  
  Answer = []
  
  Counter = 0
  Length = len(Original)
  
  while (Counter < Length):
  
    Total = 0
    Cursor = 0
    Span = len(Original)
    
    while (Cursor < Span):
      
      Value = Original[Cursor]
      
      if (Cursor == Counter):
        Cursor += 1
      else:
        Total += Value
        Cursor += 1
    
    Answer.append(Total)
    Counter += 1
    
  return Answer

