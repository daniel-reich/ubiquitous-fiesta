
import math
​
def number_pairs(txt):
​
  Blocks = txt.split(" ")
  Blocks = Blocks[1:]
  
  Unique = Blocks
  Unique = set(Blocks)
  Unique = list(Unique)
  Unique = sorted(Unique)
  
  Total = 0
  
  Counter = 0
  Length = len(Unique)
  
  while (Counter < Length):
    Wanted = Unique[Counter]
    Items = Blocks.count(Wanted)
    Pairs = math.floor(Items/2)
    Total += Pairs
    Counter += 1
  
  return Total

