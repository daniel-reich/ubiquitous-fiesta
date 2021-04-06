
def rps(p1, p2):
  if p1 == p2: return "It's a draw"
  if p1 == 'Rock':
    if p2 == 'Paper': return "The winner is p2"
    elif p2 == 'Scissors': return "The winner is p1"
  elif p1 == 'Paper':
    if p2 == 'Scissors': return "The winner is p2"
    elif p2 == 'Rock': return "The winner is p1"
  else:
    if p2 == 'Rock': return "The winner is p2"
    elif p2 == 'Paper': return "The winner is p1"

