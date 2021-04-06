
def briscola_score(my_deck1, my_deck2):
  value = {'A':11,'3':10,'K':4,'Q':3,'J':2}
  score = sum(value.get(card[0], 0) for card in my_deck1 + my_deck2)
  if score > 120: return 'You Win!'
  if score < 120: return 'You Lose!'
  return 'Draw!'

