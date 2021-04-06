
from random import shuffle
​
def gen_deck():
  deck = [(rank, suit) for suit in 'dchs' for rank in list(range(2, 15))]
  shuffle(deck)
  return deck

