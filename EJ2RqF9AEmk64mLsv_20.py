
def lottery(ticket, win):
  w=0
  for c,n in ticket:
    if chr(n) in c:
      w+=1
  if w>=win:
    return "Winner!"
  return "Loser!"

