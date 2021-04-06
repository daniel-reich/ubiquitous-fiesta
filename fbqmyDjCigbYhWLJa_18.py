
def split_into_buckets(phrase, n):
  
  Blocks = []
​
  Words = phrase.split(" ")
​
  Length = len(Words)
​
  Passage = ""
​
  Counter = 0
  
  while (Counter < Length):
    
    Width = len(Passage)
    Item = Words[Counter]
    Span = len(Item)
    
    if (Span > n):
      Counter += Length
    elif (Width + Span > n):
      Complete = Passage.rstrip(" ")
      Blocks.append(Complete)
      Passage = Item + " "
      Counter += 1
    else:
      Passage = Passage + Item + " "
      Counter += 1
​
  if (Width > 0):
​
    Complete = Passage.rstrip(" ")
    Blocks.append(Complete)
​
  return Blocks

