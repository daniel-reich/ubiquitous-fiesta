
def lottery(ticket, win):
  return ['Loser!', 'Winner!'][sum(any(ord(x)==s[-1] for x in s[0]) for s in ticket)>=win]

