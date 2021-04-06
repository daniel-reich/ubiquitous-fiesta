
def sum_round(num):
  
  Components = []
  Power = 0
  Text = str(num)
  
  Cursor = len(Text) - 1
  
  while (Cursor >= 0):
    
    Item = Text[Cursor]
    
    Digit = int(Item)
    Score = Digit * (10 ** Power)
    
    if (Score != 0):
      Passage = str(Score)
      Components.append(Passage)
    
    Power += 1
    Cursor -= 1 
  
  Link = " "
  Answer = Link.join(Components)
  return Answer

