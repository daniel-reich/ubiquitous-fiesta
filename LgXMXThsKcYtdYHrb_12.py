
def split_and_delimit(txt, num, delimiter):
  
  Passage = ""
  
  Counter = 0
  Length = len(txt)
  
  
  while (Counter < Length):
    
    Item = txt[Counter]
    
    if (Counter % num == 0) and (Counter != 0):
      Passage = Passage + delimiter
      Passage = Passage + Item
      Counter += 1
    else:
      Passage = Passage + Item
      Counter += 1
  
  return Passage

