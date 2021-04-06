
def lottery(ticket, win):
  count = 0
  
  for a, b in ticket:
    if b in list(map(ord, a)):
       count += 1
       
  return 'Winner!' if count >= win else 'Loser!'

