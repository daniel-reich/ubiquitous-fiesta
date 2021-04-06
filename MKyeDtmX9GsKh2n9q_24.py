
import random
​
​
def gen_deck():
  deck = []
  for rank in range(2, 15):
    for color in ('c', 'h', 's', 'd'):
      deck.append((rank,color))
  random.shuffle(deck)
  return deck

