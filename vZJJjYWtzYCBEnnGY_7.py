
def score(list_of_cards):
  running_score = 0
  score_dictionary = {'A':11,'3':10,'K':4,'Q':3,'J':2}
  for card in list_of_cards:
    card_rank = card[0]
    running_score += score_dictionary.get(card_rank, 0)
  return running_score
  
def briscola_score(my_deck1, my_deck2):
  score_to_beat = 120 - score(my_deck1)
  if score(my_deck2) > score_to_beat:
    return "You Win!"
  elif score(my_deck2) < score_to_beat:
    return "You Lose!"
  else:
    return "Draw!"

