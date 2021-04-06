
def largest_even(lst):
  
  Evens = []
  
  for x in lst:
    if (x % 2 == 0):
      Evens.append(x)
  
  Counter = 0
  Length = len(Evens)
  Outcome = -1
  
  while (Counter < Length):
    
    Attempt = Evens[Counter]
    
    if (Attempt > Outcome):
      Outcome = Attempt
      Counter += 1
    else:
      Counter += 1
  
  return Outcome

