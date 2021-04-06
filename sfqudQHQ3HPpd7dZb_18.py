
def rps(p1, p2):
  x, y, z = "Rock", "Paper", "Scissors"
  if p1 == p2:
    return "It's a draw"
  elif p1 == x and p2 == z or p1 == y and p2 == x or p1 == z and p2 == y:
    return "The winner is p1"
  return "The winner is p2"

