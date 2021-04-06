
def bugger(num):
  
  Steps = 0
  
  Text = str(num)
  Length = len(Text)
  
  while (Length > 1):
    
    Score = 1
    
    Cursor = 0
    Span = len(Text)
    
    while (Cursor < Span):
      Value = int(Text[Cursor])
      Score *= Value
      Cursor += 1
    
    Steps += 1
    Text = str(Score)
    Length = len(Text)
  
  return Steps

