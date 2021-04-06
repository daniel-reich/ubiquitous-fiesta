
def numbers_need_friends_too(n):
  
  Text = str(n)
  
  Blocks = []
  Batch = Text[0]
  
  Counter = 1
  Length = len(Text)
  
  while (Counter < Length):
    
    Item_A = Batch[-1]
    Item_B = Text[Counter]
    
    if (Item_A != Item_B) and (len(Batch) == 1):
      Batch = Batch + Item_A + Item_A
      Blocks.append(Batch)
      Batch = Item_B
      Counter += 1
    elif (Item_A != Item_B) and (len(Batch) > 1):
      Blocks.append(Batch)
      Batch = Item_B
      Counter += 1
    else:
      Batch = Batch + Item_B
      Counter += 1
  
  if (len(Batch) == 1):
    Batch = Batch + Batch[-1] + Batch[-1]
    Blocks.append(Batch)
  else:
    Blocks.append(Batch)
  
  Link = ""
  Merged = Link.join(Blocks)
  Answer = int(Merged)
  return Answer

