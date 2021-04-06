
def briscola_score(my_deck1,my_deck2):
  pts=0
  for card in my_deck1:
    if card[0]=='A':
      pts+=11
    elif card[0]=='3':
      pts+=10
    elif card[0]=='K':
      pts+=4
    elif card[0]=='Q':
      pts+=3
    elif card[0]=='J':
      pts+=2
  print(pts)
  pts2=0
  for card in my_deck2:
    if card[0]=='A':
      pts2+=11
    elif card[0]=='3':
      pts2+=10
    elif card[0]=='K':
      pts2+=4
    elif card[0]=='Q':
      pts2+=3
    elif card[0]=='J':
      pts2+=2
  print(pts2)
  if pts2>=(120-pts)+1:
    return 'You Win!'
  elif pts2==(120-pts):
    return 'Draw!'
  else:
    return 'You Lose!'

