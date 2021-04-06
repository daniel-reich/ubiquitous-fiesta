
def expanded_form(num):
  
  #   Converting 'num' to Text
  Text = str(num)
  Blocks = Text.split(".")
  
  Whole = Blocks[0]
  Part = Blocks[1]
  
  #   Buckets for Passages of Text
  Pieces = []
  
  #   Going Through Whole Number Section
  Cursor = len(Whole) - 1
  Multiple = 1
  
  while (Cursor >= 0):
    
    Item = Whole[Cursor]
    
    if (Item == "0"):
      Multiple *= 10
      Cursor -= 1
    else:
      Score = int(Item) * Multiple
      Passage = str(Score)
      Pieces.insert(0, Passage)
      Multiple *= 10
      Cursor -= 1
  
  #   Going Through Part Number Section
  Multiple = 10
  
  Cursor = 0
  Length = len(Part)
  
  while (Cursor < Length):
    
    Item = Part[Cursor]
    
    if (Item == "0"):
      Multiple *= 10
      Cursor += 1
    else:
      Passage = Item + "/" + str(Multiple)
      Pieces.append(Passage)
      Multiple *= 10
      Cursor += 1
  
  #   Building and Giving Answer
  Link = " + "
  Answer = Link.join(Pieces)
  return Answer

