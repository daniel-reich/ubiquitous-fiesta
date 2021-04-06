
def count_number(lst):
  
  Text = str(lst)
  Text = Text.replace("[","")
  Text = Text.replace("]","")
  Text = Text.replace("'","")
  Text = Text.replace(" ","")
  
  Blocks = Text.split(",")  
  
  Events = 0
  
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    
    Item = Blocks[Counter]
        
    if (Item == ""):
      Counter += 1
    
    elif (Item.isdigit()):
      Events += 1
      Counter += 1
    
    elif ("." in Item):
      First = str(Item[0])
            
      if (First.isdigit()):
        Events += 1
        Counter += 1
    
      else:
        Counter += 1
                
    else:
      Counter += 1
  
  return Events

