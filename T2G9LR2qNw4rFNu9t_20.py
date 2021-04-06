
def chunk(array, size):
  
  Answer = []
  
  Counter = 0
  Length = len(array)
  
  while (Counter < Length):
  
    Batch = []
    Added = 0
    Required = size
    
    while (Added < Required) and (Counter < Length):
      Item = array[Counter]
      Batch.append(Item)
      Added += 1
      Counter += 1
    
    Answer.append(Batch)
    
  return Answer

