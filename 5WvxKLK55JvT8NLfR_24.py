
def diag_dom(lst):
  
  Target = 0
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
  
    Value = abs(lst[Counter][Counter])
    Target += Value
    Counter += 1
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Row = lst[Counter]
    
    Score = 0
    
    Cursor = 0
    End = len(Row)
    
    while (Cursor < End):
      
      Item = abs(Row[Cursor])
      Score += Item
      Cursor += 1
    
    Value = abs(lst[Counter][Counter])
    Score -= Value
    
    if (Score >= Value):
      return False
    else:
      Counter += 1
  
  return True

