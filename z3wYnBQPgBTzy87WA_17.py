
def rps(p1, p2):
  wl = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
  return 'TIE' if p1 == p2 else 'Player {} wins'.format([1, 2][wl[p2] == p1])

