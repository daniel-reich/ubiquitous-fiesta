
def lottery(ticket, win):
  return 'Winner!' if sum(1 for t in ticket if any(ord(c) == t[1] for c in t[0])) >= win else 'Loser!'

