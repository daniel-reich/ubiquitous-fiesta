
from random import shuffle
​
def gen_deck():
  result_card = []
  card_type = ("d", "c", "h", "s")
  
  for card in card_type:
    for index in range(2, 15):
      result_card.append((index, card))
      
  shuffle(result_card)
  return result_card

