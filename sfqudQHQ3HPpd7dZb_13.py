
def rps(p1, p2):
  if p1 == p2: return "It's a draw"
  if p1 == 'Rock':
    if p2 == 'Scissors': return "The winner is p1"
    return "The winner is p2"
  if p1 == 'Paper':
    if p2 == 'Rock': return "The winner is p1"
    return "The winner is p2"
  if p1 == 'Scissors':
    if p2 == 'Paper': return "The winner is p1"
    return "The winner is p2"

