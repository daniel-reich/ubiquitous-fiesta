
def lottery(ticket, win):
  results = []
  
  for i, j in ticket:
    results += [ord(k) == j for k in i]
    
  return ['Loser!', 'Winner!'][sum(results) >= win]

