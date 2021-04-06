
def is_scalable(lst):
  
  Length = len(lst)
  
  if (Length < 2):
    return True
  
  Value_1A = lst[0]
  Value_1B = lst[1]
  Scale_01 = abs(Value_1B - Value_1A)
  
  if (Scale_01 > 5):
    return False
  
  Value_2A = lst[-1]
  Value_2B = lst[-2]
  Scale_02 = abs(Value_2B - Value_2A)
  
  if (Scale_02 > 5):
    return False
  
  Previous = 0
  Current = 1
  Next = 2
  Length = len(lst)
  
  while (Next < Length):
    
    Value_3A = lst[Previous]
    Value_3B = lst[Current]
    Value_3C = lst[Next]
    
    Scale_03A = abs(Value_3B - Value_3A)
    Scale_03B = abs(Value_3B - Value_3C)
    
    if (Scale_03A > 5) or (Scale_03B > 5):
      return False
    else:
      Previous += 1
      Current += 1
      Next += 1
  
  return True

