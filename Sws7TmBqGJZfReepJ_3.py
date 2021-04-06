
def make_anagram(a, b):
  
  Combined = a + b
  
  Chunks = []
  
  Counter = 0
  Length = len(Combined)
  
  while (Counter < Length):
    
    Item = Combined[Counter]
    
    if (Item in Chunks):
      Counter += 1
    else:
      Chunks.append(Item)
      Counter += 1
  
  Total = 0
  
  Counter = 0
  Length = len(Chunks)
  
  while (Counter < Length):
    
    Item = Chunks[Counter]
    
    Score_A = a.count(Item)
    Score_B = b.count(Item)
    
    Removals = abs(Score_A - Score_B)
    Total += Removals
    
    Counter += 1
    
  return Total

