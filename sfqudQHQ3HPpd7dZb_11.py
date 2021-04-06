
def rps(p1, p2):
  if p1 == p2:
    return "It's a draw"
  beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
  return "The winner is {}".format("p1" if beats[p1] == p2 else "p2")

