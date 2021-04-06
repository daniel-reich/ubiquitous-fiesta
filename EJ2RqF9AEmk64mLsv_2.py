
def lottery(ticket, win):
  return ["Loser!", "Winner!"][sum(chr(x[1]) in x[0] for x in ticket) >= win]

