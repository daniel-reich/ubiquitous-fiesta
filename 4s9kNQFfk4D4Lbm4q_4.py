
def ABA(s):
  
  CODE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  Block = "A"
  
  Counter = 1
  Length = CODE.index(s)
  
  while (Counter <= Length):
    
    Letter = CODE[Counter]
    Batch = Block + Letter + Block
    Block = Batch
    Counter += 1
  
  return Block

