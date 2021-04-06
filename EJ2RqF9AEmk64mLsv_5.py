
def lottery(ticket, win):
  fu = sum(ord(c) == n for s, n in ticket for c in s)
  return "Loser!" if fu < win else "Winner!"

