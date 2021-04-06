
def babbage(n):
  
  Failsafe = 0
  Candidate = 1
  
  while (Failsafe == 0):
  
    Score = Candidate * Candidate
    
    Text_A = str(Score)
    Text_B = str(n)
  
    if (Text_A.endswith(Text_B)):
      Failsafe += 1
    else:
      Candidate += 1
  
  if (n == 269696) and (Candidate == 99736):
    return "Babbage was correct!"
  elif (n == 269696) and (Candidate != 99736):
    return "Babbage was incorrect!"
  else:
    return Candidate

