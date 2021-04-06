
def almost_uniform(nums):
  
  Ordered = set(nums)
  Ordered = sorted(list(Ordered))
  
  Answer = 0
  
  First = 0
  Second = 1
  Length = len(Ordered)
  
  while (Second < Length):
    
    Value_A = Ordered[First]
    Value_B = Ordered[Second]
    Difference = Value_B - Value_A
    
    Score_A = nums.count(Value_A)
    Score_B = nums.count(Value_B)
    Total = Score_A + Score_B
    
    if (Difference != 1):
      First += 1
      Second += 1
    elif (Total <= Answer):
      First += 1
      Second += 1
    else:
      Answer = Total
      First += 1
      Second += 1
  
  return Answer

