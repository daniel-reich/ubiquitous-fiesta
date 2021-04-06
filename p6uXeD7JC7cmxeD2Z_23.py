
def calculate_score(games):
  aWins = 0
  bWins = 0
  for row in games:
    a,b = row
    if a==b: continue
    if (a=="R" and b=="S") or (a=="P" and b=="R") or (a=="S" and b=="P"):
      aWins+=1
    else:
      bWins +=1
  if aWins>bWins: return "Abigail" 
  if bWins>aWins: return "Benson"
  return "Tie"

