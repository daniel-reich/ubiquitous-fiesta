
def get_primiera_score(deck):
  if set(card[1] for card in deck) != {'h','d','s','c'}:
    return 0
  
  val = {'2':12,'3':13,'4':14,'5':15,'6':18,'7':21,'J':10,'Q':10,'K':10,'A':16}
  score = 0
  for i in 'hdsc':
    score += max([val[card[0]] for card in deck if card[1] == i])
  return score

