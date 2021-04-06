
def count_same_ends(txt):
  
  # Removing Punctuation
  
  Allowed = " abcdefghijklmnopqrstuvwxyz"
  Revision_One = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Item = txt[Counter].lower()
    
    if (Item in Allowed):
      Revision_One = Revision_One + Item.lower()
      Counter += 1
    else:
      Counter += 1
  
  # Splitting into Word Blocks
  Blocks = Revision_One.split(" ")
  
  # Bucket for Answer
  Answer = 0
  
  # Checking Ends of Words
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]
    Span = len(Item)
    First = Item[0]
    Last = Item[-1]
    
    if (First == Last) and (Span > 1):
      Answer += 1
      Counter += 1
    else:
      Counter += 1
  
  # Giving Answer
  return Answer

