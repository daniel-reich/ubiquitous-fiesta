
def rps(p1, p2):
  if p1 == p2:
    return "It's a draw"
  if p1 == "Rock" and p2 == "Scissors" or p1 == "Scissors" and p2 == "Paper" or p1 == "Paper" and p2 == "Rock":
    return "The winner is p1"
  else:
    return "The winner is p2"

