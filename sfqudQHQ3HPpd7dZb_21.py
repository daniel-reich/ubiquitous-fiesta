
def rps(p1, p2):
  d={'Paper':'Rock','Rock':'Scissors','Scissors':'Paper'}
  return "It's a draw" if p1==p2 else "The winner is p1" if d[p1]==p2 else "The winner is p2"

