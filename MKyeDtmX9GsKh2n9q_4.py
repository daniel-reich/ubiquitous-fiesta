
from random import shuffle
def gen_deck():
  deck = [(i, j) for i in range(2,15) for j in "hcsd"]
  shuffle(deck)
  return deck

