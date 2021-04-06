
def rps(p1,p2):
  p1 = p1.lower()
  p2 = p2.lower()
  if p1 == p2:
    return "It's a draw"
  if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
    return 'The winner is p1'
  return 'The winner is p2'

