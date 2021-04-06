
def leader(lst):
  
  Values = lst
  
  Sequence = []
  Sequence.append(lst[-1])
  
  Cursor = -2
  Length = len(lst)
  End = Length * -1
  
  while (Cursor >= End):
    Item_A = Values[Cursor]
    Item_B = Sequence[0]
    
    if (Item_A > Item_B):
      Sequence.insert(0,Item_A)
      Cursor -= 1
    else:
      Cursor -= 1
  
  return Sequence

