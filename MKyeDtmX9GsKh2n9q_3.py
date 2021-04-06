
from random import shuffle
def gen_deck():
  rank = range(2,15)
  suit = 'cdhs'
  deck = [(r,s) for s in suit for r in rank]
  shuffle(deck)
  return deck

