
def possibly_perfect(key, answers):
  
  Guesses = key
  Required = answers
​
  Answered = 0
  Right = 0
  Wrong = 0
​
  Counter = 0
  Length = len(answers)
  
  while (Counter < Length):
        
    Answer = str(Guesses[Counter])
    Correct = str(Required[Counter])
    
    if (Answer == "_"):
      Counter += 1
    elif (Answer == Correct) and (Answer != "_"):
      Answered += 1
      Right += 1
      Counter += 1
    elif (Answer != Correct) and (Answer != "_"):
      Answered += 1
      Wrong += 1
      Counter += 1
    else:
      Counter += 1
  
  if (Answered == Right) or (Answered == Wrong):
    return True
  else:
    return False

