
def add_bill(money):
   
  Blocks = money.split(",")
  
  Total = 0
  
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Text = str(Blocks[Counter])
    
    if ("d" not in Text):
      Counter += 1
    else:
      Text = Text.replace("d","")
      Text = Text.replace("k","000")
      Value = int(Text)
      Total += Value
      Counter += 1
  
  return Total

