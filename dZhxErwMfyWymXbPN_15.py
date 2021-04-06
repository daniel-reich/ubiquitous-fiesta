
def hangman(phrase, lst):
  
  Status = ""
  CODE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  Counter = 0
  Length = len(phrase)
  
  while (Counter < Length):
  
    Item = phrase[Counter]
    
    if (Item.upper() in lst) or (Item.lower() in lst):
      Status = Status + Item
      Counter += 1
    elif (Item.upper() not in CODE):
      Status = Status + Item
      Counter += 1
    else:
      Status = Status + "-"
      Counter += 1
  
  return Status

