
def rps(p1,p2):
  if p1 == p2:
    return "It's a draw"
  elif p1 == "Rock":
    winner = "p1" if p2 == "Scissors" else "p2"
  elif p1 == "Paper":
    winner = "p1" if p2 == "Rock" else "p2"
  elif p1 == "Scissors":
    winner = "p1" if p2 == "Paper" else "p2"
  return "The winner is " + winner

