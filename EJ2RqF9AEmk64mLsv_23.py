
def lottery(ticket, win):
  mini_wins = 0
  for t in ticket:
    for s in t[0]:
      if ord(s) == t[1]:
        mini_wins += 1
  if mini_wins >= win:
    return 'Winner!'
  return 'Loser!'

