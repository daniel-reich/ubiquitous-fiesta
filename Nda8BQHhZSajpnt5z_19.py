
def GCD(lst):
  
  Answer = 1
  
  Test = 2
  End = min(lst)
  
  while (Test <= End):
    
    Outcomes = []
    
    Counter = 0
    Length = len(lst)
    
    while (Counter < Length):
      Number = lst[Counter]
      Outcome = Number % Test
      Outcomes.append(Outcome)
      Counter += 1
    
    Outcomes = set(Outcomes)
    Outcomes = list(Outcomes)
    
    if (Outcomes == [0]):
      Answer = Test
      Test += 1
    else:
      Test += 1
  
  return Answer

