
def lottery(ticket, win):
  count = 0
  for e in ticket:
    if e[0].count(chr(e[1])) == 1:
      count += 1
  return 'Winner!' if count >= win else 'Loser!'

