
def amount_fib(n):
  
  if (n == 0):
    return 0
  
  if (n == 1):
    return 1
  
  Sequence = [0, 1]
  New = Sequence[-2] + Sequence[-1]
  
  while (New < n):
    New = Sequence[-2] + Sequence[-1]
    Sequence.append(New)
  
  Events = 0
  Counter = 0
  Length = len(Sequence)
  
  while (Counter < Length):
    
    Item = Sequence[Counter]
    
    if (Item < n):
      Events += 1
      Counter += 1
    else:
      Counter += 1
      
  return Events

