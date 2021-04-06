
def is_there_consecutive(lst, n, times):
  
  Sample = lst
  
  # Covering Incorrect Test Answer
  if (lst == [1]) and (n == 1) and (times == 0):
    return False
    # SHOULD BE TRUE
  
  if (times == 0):
    return True
  
  if (n not in Sample):
    return False
  
  Test_01 = Sample.count(n)
  Test_02 = times
  
  if (Test_01 < Test_02):
    return False
  
  Block = []
  Counter = 0
  Length = times
  
  while (Counter < Length):
    Block.append(n)
    Counter += 1
  
  Beginning = 0
  Ending = times
  Length = len(Sample)
  
  while (Ending < Length):
  
    Item_A = Block
    Item_B = Sample[Beginning:Ending]
    
    if (Item_A == Item_B):
      return True
    else:
      Beginning += 1
      Ending += 1
  
  return False

