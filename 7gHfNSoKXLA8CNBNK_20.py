
def sim_prop_frac(max_den):
  
  Answer = 0
  Scores = []
  
  Top = 1
  Bottom = 2
  
  while (Bottom <= max_den):
  
    while (Top < Bottom):
      
      Outcome = Top / Bottom
    
      if (Outcome in Scores):
        Top += 1
      else:
        Scores.append(Outcome)
        Answer += 1
        Top += 1
    
    Top = 1
    Bottom += 1
      
  return Answer

