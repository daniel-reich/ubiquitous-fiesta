
def rps(p1,p2):
  if len(p1) == len(p2):
    return "It's a draw"
  p1_winning_stuations = [("Paper", "Rock"), ("Rock", "Scissors"), ("Scissors", "Paper")]
  if (p1,p2) in p1_winning_stuations:
    return "The winner is p1"
  else:
    return "The winner is p2"

