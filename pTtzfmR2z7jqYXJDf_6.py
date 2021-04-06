
def possible_palindrome(txt):
  
  # Establishing Unique Letters
  
  Sample = str(txt)
  SL = len(Sample)
  
  Unique = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Letter = Sample[Counter]
    
    if (Letter in Unique):
      Counter += 1
    else:
      Unique.append(Letter)
      Counter += 1
  
  # Establishing Frequencies of Unique Letters
  
  Sample = str(txt)
  
  Evens = []
  Odds = []
  
  Counter = 0
  Length = len(Unique)
  
  while (Counter < Length):
    Letter = Unique[Counter]
    Occurrences = Sample.count(Letter)
    
    if (Occurrences % 2 == 0):
      Evens.append(Letter)
      Counter += 1
    else:
      Odds.append(Letter)
      Counter += 1
  
  # Establishing Viability of Palindrome
  
  SL = len(Sample)
  OL = len(Odds)
  EL = len(Evens)
  
  if (SL % 2 == 0) and (OL == 0):
    return True
  elif (SL % 2 != 0) and (OL == 1):
    return True
  else:
    return False

