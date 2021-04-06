
############################################################
#   Sub Function
############################################################
​
def FNC_Position_Finder(Unique_Scores, Current_Score):
​
  Counter = 0
  Length = len(Unique_Scores)
  
  while (Counter < Length):
  
    Target = Unique_Scores[Counter]
    
    if (Current_Score >= Target):
      return Counter + 1
    else:
      Counter += 1
      
  return Counter + 1
​
############################################################
#   MAIN FUNCTION
############################################################
​
def climbing_leaderboard(ranked, player):
  
  # Establishing Unique Scores of 'ranked' Players
  
  Unique_Scores = []
  
  Counter = 0
  Length = len(ranked)
  
  while (Counter < Length):
  
    Item = ranked[Counter]
    
    if (Item in Unique_Scores):
      Counter += 1
    else:
      Unique_Scores.append(Item)
      Counter += 1
  
  # Establishing Progressive Status of Player
  
  Progressive_Status = []
  
  Counter = 0
  Length = len(player)
  
  while (Counter < Length):
    Current_Score = player[Counter]
    New_Rank = FNC_Position_Finder(Unique_Scores, Current_Score)
    Progressive_Status.append(New_Rank)
    Counter += 1
    
  # Giving Answer
  return Progressive_Status

