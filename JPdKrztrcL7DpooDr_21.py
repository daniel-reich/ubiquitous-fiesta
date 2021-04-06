
def collatz(n):
  
  if (n == 1):
    return [0, 1]
  
  Number = n
  Sequence = []
  Sequence.append(Number)
  
  while (Number != 1):
    
    if (Number % 2 == 0):
      Number /= 2
      Number = int(Number)
      Sequence.append(Number)
    else:
      Number *= 3
      Number += 1
      Sequence.append(Number)
  
  Circuits = len(Sequence)
  Highest = max(Sequence)
  
  Answer = []
  Answer.append(Circuits - 1)
  Answer.append(Highest)
  
  return Answer

