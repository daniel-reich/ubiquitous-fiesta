
def leaderboards(users):
  
  Names = []
  Scores = []
  Reputations = []
    
  Counter = 0
  Length = len(users)
    
  while (Counter < Length):
        
    Thing = users[Counter]
        
    Names.append(Thing["name"])
    Scores.append(Thing["score"])
    Reputations.append(Thing["reputation"])
        
    Counter += 1
        
  Overall = []
  Sorted = []
​
  Counter = 0
  Length = len(Scores)
  
  while (Counter < Length):
    Part1 = (Scores[Counter]) * 1
    Part2 = (Reputations[Counter]) * 2
    TrueScore = Part1 + Part2
    Overall.append(TrueScore)
    Sorted.append(TrueScore)
    Counter += 1
  
  Sorted = sorted(Sorted, reverse = True)
​
  Revised = []
  
  OC = 0
  OL = len(Overall)
  
  SC = 0
  SL = len(Sorted)
    
  if (Revised == []):
    RL = 0
  else:
    RL = len(Revised)
    
  while (RL < SL):
  
    Checking = Overall[OC]
    Seeking = Sorted[SC]
    
    if (Checking == Seeking):
      
      Dictionary = {}
      Dictionary["name"] = Names[OC]
      Dictionary["score"] = Scores[OC]
      Dictionary["reputation"] = Reputations[OC]
      
      Revised.append(Dictionary)
      RL = len(Revised)
      SL = len(Sorted)
      OC = 0
      SC += 1
    
    else:
      OC += 1
  
  return Revised

