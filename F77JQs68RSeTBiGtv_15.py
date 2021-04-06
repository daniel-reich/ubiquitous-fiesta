
def diamond_sum(n):
  
  #   Building Diamond
  
  Diamond = []
  
  Number = 1
  Ceiling = n * n
  
  while (Number <= Ceiling):
    
    Batch = []
    Added = 0
    Required = n
    
    while (Added < Required):
      Batch.append(Number)
      Added += 1
      Number += 1
    
    Diamond.append(Batch)
  
  #   Bucket for Total
  Total = 0
  
  #   Going Down from Top Middle
  Cursor_A = int((n - 1) / 2)
  Cursor_B = int((n - 1) / 2)
  Row = 0
  
  while (Cursor_A >= 0):
    
    if (Cursor_A == Cursor_B):
      
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Cursor_A -= 1
      Cursor_B += 1
      Row += 1
  
    else:
    
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Value_B = Diamond[Row][Cursor_B]
      Total += Value_B
      
      Cursor_A -= 1
      Cursor_B += 1
      Row += 1
  
  #   Going Up from Bottom Middle
  Cursor_A = int((n - 1) / 2)
  Cursor_B = int((n - 1) / 2)
  Row = -1
  
  while (Cursor_A > 0):
    
    if (Cursor_A == Cursor_B):
      
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Cursor_A -= 1
      Cursor_B += 1
      Row -= 1
  
    else:
    
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Value_B = Diamond[Row][Cursor_B]
      Total += Value_B
      
      Cursor_A -= 1
      Cursor_B += 1
      Row -= 1
  
  #   Giving Answer
  return Total

