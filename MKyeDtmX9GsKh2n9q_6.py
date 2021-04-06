
from random import randint
def gen_deck():
  cards = (2,3,4,5,6,7,8,9,10,11,12,13,14)
  suits = ('c','d','s','h')
  deck = [(c,s) for s in suits for c in cards]
  
  shuffled = []
  while deck:
    shuffled.append(deck.pop(randint(0,len(deck)-1)))
  return shuffled

