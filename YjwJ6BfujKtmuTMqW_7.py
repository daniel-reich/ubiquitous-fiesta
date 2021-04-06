
def dice_game(scores):
  p = ['p1', 'p2', 'p3', 'p4']
  scrs_iter = iter(scores)
  
  def value(p): # value sutiable to compare/sort
    a, b = p[1][0], p[1][1]
    return (a+b)*7 +a
    
  while len(p) > 1:
    # play round
    rnd = list(zip(p, scrs_iter)) # list of (p, (x, y))
    #sort players
    rnd = sorted(rnd, key=value)
    if value(rnd[0]) == value(rnd[1]): continue
    p.remove(rnd[0][0])
  return p[0]

