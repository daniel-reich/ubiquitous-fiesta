
def rps(p1, p2):
  p,r,s = "Paper Rock", "Rock Scissors", "Scissors Paper"
  return "The winner is p1" if any(w == p1 +' '+ p2  for w in [p,r,s]) else "The winner is p2" if any(w == p2 +' '+ p1  for w in [p,r,s]) else "It's a draw"

