
def lottery(ticket, win):
  mini_wins = sum(sum(ord(ch) == value for ch in code) for code, value in ticket)
  return ['Loser!', 'Winner!'][mini_wins >= win]

