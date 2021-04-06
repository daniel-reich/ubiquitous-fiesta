
def max_collatz(num):
  
  Sequence = []
  Sequence.append(num)
  
  while (Sequence[-1] != 1):
    
    Current = Sequence[-1]
    
    if (Current % 2 == 0):
      New = Current / 2
      Sequence.append(New)
    
    else:
      New = (Current * 3) + 1
      Sequence.append(New)
  
  return max(Sequence)

