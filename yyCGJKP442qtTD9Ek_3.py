
def sums_of_powers_of_two(n):
  
  Binary = bin(n)
  Text = str(Binary[2:])
  
  Answer = []
  Cursor = len(Text) - 1
  Multiple = 1
  
  while (Cursor >= 0):
    
    Item = Text[Cursor]
    
    if (Item == "1"):
      Answer.append(Multiple)
      Multiple *= 2
      Cursor -= 1
    else:
      Multiple *= 2
      Cursor -= 1
      
  return Answer

