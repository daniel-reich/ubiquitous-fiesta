
def modify(txt):
  
  Code = " abcdefghijklmnopqrstuvwxyz"
  Cursor = len(txt) - 1
  Passage = ""
  
  while (Cursor >= 0):
    Item = txt[Cursor]
    Score = Code.index(Item)
    Block = str(Score)
    Passage = Passage + Block
    Cursor -= 1
  
  Base_10 = int(Passage)
  Base_02 = bin(Base_10)
  Text = str(Base_02)
  Answer = int(Text[2:])
  return Answer

