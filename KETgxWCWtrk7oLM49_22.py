
def tournament_scores(Results):
  
  # Buckets for Statistical Collection on Goals
  
  A_Goals_Scored = 0
  A_Goals_Conceded = 0
  
  B_Goals_Scored = 0
  B_Goals_Conceded = 0
  
  C_Goals_Scored = 0
  C_Goals_Conceded = 0
  
  D_Goals_Scored = 0
  D_Goals_Conceded = 0
  
  # Buckets for Statistical Collection on Wins and Draws Earned
  Wins = []
  Draws = []
  
  # Tallying Goals and Results in While Loop...
  Counter = 0
  Length = len(Results)
  
  while (Counter < Length):
    
    # Pre-Tallying Variables
    
    Match = Results[Counter]
    Blocks = Match.split(" ")
    
    Home_Team = Blocks[0]
    Home_Goals = int(Blocks[1])
    
    Away_Team = Blocks[-1]
    Away_Goals = int(Blocks[-2])
    
    # Establishing Result
    
    if (Home_Goals > Away_Goals):
      Wins.append(Home_Team)
    elif (Away_Goals > Home_Goals):
      Wins.append(Away_Team)
    else:
      Draws.append(Home_Team)
      Draws.append(Away_Team)
    
    # Adjusting Home Team Goals Statistics
    if (Home_Team == "A"):
      A_Goals_Scored += Home_Goals
      A_Goals_Conceded += Away_Goals
      
    elif (Home_Team == "B"):
      B_Goals_Scored += Home_Goals
      B_Goals_Conceded += Away_Goals
      
    elif (Home_Team == "C"):
      C_Goals_Scored += Home_Goals
      C_Goals_Conceded += Away_Goals
    
    elif (Home_Team == "D"):
      D_Goals_Scored += Home_Goals
      D_Goals_Conceded += Away_Goals
    
    else:
      return "ERROR on Home Team Goal Adjustment"
      
    # Adjusting Away Team Goals Statistics
    if (Away_Team == "A"):
      A_Goals_Scored += Away_Goals
      A_Goals_Conceded += Home_Goals
      
    elif (Away_Team == "B"):
      B_Goals_Scored += Away_Goals
      B_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "C"):
      C_Goals_Scored += Away_Goals
      C_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "C"):
      C_Goals_Scored += Away_Goals
      C_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "D"):
      D_Goals_Scored += Away_Goals
      D_Goals_Conceded += Home_Goals
    
    else:
      return "ERROR on Away Team Goal Adjustment"
      
    # Moving to Next Match
    Counter += 1
    
  # Establishing Points Earned
  A_Points = (Wins.count("A") * 3) + (Draws.count("A") * 1)
  B_Points = (Wins.count("B") * 3) + (Draws.count("B") * 1)
  C_Points = (Wins.count("C") * 3) + (Draws.count("C") * 1)
  D_Points = (Wins.count("D") * 3) + (Draws.count("D") * 1)
  
  # Building Lists of Statistics for Each Team
  Batch_A = []
  Batch_A.append("A")
  Batch_A.append(A_Points)
  Batch_A.append(A_Goals_Scored)
  A_Goal_Difference = A_Goals_Scored - A_Goals_Conceded
  Batch_A.append(A_Goal_Difference)
  
  Batch_B = []
  Batch_B.append("B")
  Batch_B.append(B_Points)
  Batch_B.append(B_Goals_Scored)
  B_Goal_Difference = B_Goals_Scored - B_Goals_Conceded
  Batch_B.append(B_Goal_Difference)
  
  Batch_C = []
  Batch_C.append("C")
  Batch_C.append(C_Points)
  Batch_C.append(C_Goals_Scored)
  C_Goal_Difference = C_Goals_Scored - C_Goals_Conceded
  Batch_C.append(C_Goal_Difference)
  
  Batch_D = []
  Batch_D.append("D")
  Batch_D.append(D_Points)
  Batch_D.append(D_Goals_Scored)
  D_Goal_Difference = D_Goals_Scored - D_Goals_Conceded
  Batch_D.append(D_Goal_Difference)
  
  # Building League Table
  League_Table = []
  League_Table.append(Batch_A)
  League_Table.append(Batch_B)
  League_Table.append(Batch_C)
  League_Table.append(Batch_D)
  
  # Sorting League Table and Giving Answer
  League_Table = sorted(League_Table, key = lambda x : (-x[1], -x[2], -x[3], x[0]))
  return League_Table

