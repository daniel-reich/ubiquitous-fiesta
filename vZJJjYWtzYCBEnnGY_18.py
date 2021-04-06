
value = {'A': 11, '3':10,'K':4,'Q':3,'J':2,'2':0,'4':0,'5':0,'6':0,'7':0}
def briscola_score(my_deck1, my_deck2):
  score1 = 0
  score2 = 0
  for card in my_deck1:
    score1 = score1 + value[card[0]]
  for card in my_deck2:
    score2 = score2 + value[card[0]]  
  
  if score1 + score2 == 120:
    return "Draw!"
  elif (score1 + score2) >120:
    return "You Win!"
  else:
    return "You Lose!"

