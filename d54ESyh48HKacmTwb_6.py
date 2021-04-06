
def gcd(lst):
  
  Floor = min(lst)
  Answer = 1
  Candidate = 2
  
  while (Candidate <= Floor):
  
    Divisible = 0
    Counter = 0
    Length = len(lst)
    
    while (Counter < Length):
      
      Item = lst[Counter]
      
      if (Item % Candidate == 0):
        Divisible += 1
        Counter += 1
      else:
        Counter += 1
    
    if (Divisible == Length):
      Answer = Candidate
      Candidate += 1
    else:
      Candidate += 1
  
  return Answer

