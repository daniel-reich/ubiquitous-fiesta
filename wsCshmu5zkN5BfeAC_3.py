
def divisible_by_left(n):
​
  Answer = []
  Answer.append(False)
  
  Text = str(n)
  
  First = 0
  Second = 1
  Length = len(Text)
  
  while (Second < Length):
    
    Top = int(Text[Second])
    Bottom = int(Text[First])
    
    if (Bottom == 0) or (Top % Bottom != 0):
      Answer.append(False)
      First += 1
      Second += 1
    else:
      Answer.append(True)
      First += 1
      Second += 1
      
  return Answer

