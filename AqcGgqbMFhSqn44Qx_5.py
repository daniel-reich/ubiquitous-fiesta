
import re
​
def tweet(txt):
  
  Blocks = re.findall("#\w+|@\w+",txt)
  
  Passage = ""
  
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]
    Passage = Passage + Item + " "
    Counter += 1
  
  Passage = Passage.rstrip(" ")
  
  return Passage

