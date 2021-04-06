
def rps(p1,p2):
  if p1 == p2:
    return "It's a draw"
  if p1 == 'Scissors' and p2 == 'Rock':
    return "The winner is p2"
  if p1 == 'Rock' and p2 == 'Scissors':
    return "The winner is p1"
  if p1 == 'Paper' and p2 == 'Rock':
    return "The winner is p1"
  if p1 == 'Rock' and p2 == 'Paper':
    return "The winner is p2" 
  if p1 == 'Paper' and p2 == 'Scissors':
    return "The winner is p2"
  if p1 == 'Scissors' and p2 == 'Paper':
    return "The winner is p1"

