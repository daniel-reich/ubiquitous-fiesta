
def lottery(ticket, win):
  wygrana = 0 
  for i in range(len(ticket)):
    if chr(ticket[i][1]) in ticket[i][0]:
      wygrana+=1
  if wygrana>=win:
    return 'Winner!'
  return 'Loser!'

