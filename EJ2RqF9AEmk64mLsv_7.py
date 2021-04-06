
def lottery(ticket, win):
  return ['Loser!', 'Winner!'][sum(ord(i) == y for x, y in ticket for i in x) >= win]

