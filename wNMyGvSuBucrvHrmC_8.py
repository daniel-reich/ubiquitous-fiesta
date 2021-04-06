
def number_of_repeats(Sample):
​
  Length = len(Sample)
  
  Multiples_A = []
  Multiples_B = []
  
  Tester = 1
  
  while (Tester <= Length):
    
    if (Length % Tester == 0):
      Number_A = Tester
      Number_B = Length / Tester
      Multiples_A.append(Number_A)
      Multiples_B.append(Number_B)
      Tester += 1
    else:
      Tester += 1
  
  Counter = 0
  Length = len(Multiples_A)
  
  while (Counter < Length):
    
    Finish = Multiples_A[Counter]
    Batch = Sample[0:Finish]
    Multiple = int(Multiples_B[Counter])
  
    if (Batch * Multiple == Sample):
      return Multiple
    else:
      Counter += 1

