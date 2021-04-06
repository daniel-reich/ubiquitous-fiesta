
def lottery(ticket, win):
  tot = sum(any(map(lambda c: ord(c) == n, t)) for t, n in ticket)
  return ('Loser!', 'Winner!')[tot >= win]

