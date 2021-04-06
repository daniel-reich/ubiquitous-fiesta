
def single_occurrence(txt):
  
  txt = txt.upper()
  Answer = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Item = txt[Counter]
    Events = txt.count(Item)
    
    if (Events == 1):
      Answer = Item
      return Answer
    else:
      Counter += 1
      
  return Answer

