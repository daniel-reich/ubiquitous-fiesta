
def diamond_arrays(x):
​
  Answer = []
  Required = 1
  
  while (Required <= x):
    
    Added = 0
    Batch = []
    
    while (Added < Required):
      Batch.append(Required)
      Added += 1
      
    Answer.append(Batch)
    Required += 1
  
  while (Required >= x):
    Required -= 1
  
  while (Required > 0):
    
    Added = 0
    Batch = []
    
    while (Added < Required):
      Batch.append(Required)
      Added += 1
      
    Answer.append(Batch)
    Required -= 1
  
  return Answer

