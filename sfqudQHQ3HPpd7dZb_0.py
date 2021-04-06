
def rps(p1,p2):
  v = {'Rock':1, 'Paper':2, 'Scissors':3}
  return ["It's a draw", 'The winner is p1', 'The winner is p2'][v[p1]-v[p2]]

