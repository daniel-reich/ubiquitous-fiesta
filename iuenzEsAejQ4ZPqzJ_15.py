
def mystery_func(num):
  
  Answer = ""
  
  Target = num
  Score = 0
  
  Failsafe = 0
  
  while (Failsafe == 0):
    
    if (Score == 0) and (Score + 2 <= Target):
      Answer = Answer + "2"
      Score +=2
    elif (Score != 0) and (Score * 2 <= Target):
      Answer = Answer + "2"
      Score *= 2
    else:
      Failsafe += 1
    
  Remainder = Target - Score
  Answer = Answer + str(Remainder)
  Answer = int(Answer)
  
  return Answer

