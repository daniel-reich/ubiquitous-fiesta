
def lottery(ticket, win):
  d = ["Loser!", "Winner!"]
  return d[sum(1 for k,v in ticket for c in k if ord(c) == v) >= win]

