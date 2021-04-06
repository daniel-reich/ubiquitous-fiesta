
def is_slidey(n):
  
  Text = str(n)
  
  Previous = 0
  Current = 1
  Length = len(Text)
  
  while (Current < Length):
    Value_A = int(Text[Previous])
    Value_B = int(Text[Current])
    Difference = int(abs(Value_A - Value_B))
    
    if (Difference == 1):
      Previous += 1
      Current += 1
    else:
      return False
  
  return True

