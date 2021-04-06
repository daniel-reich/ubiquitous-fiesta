
from random import shuffle
​
def gen_deck():
    cards = [(rank, suit) for rank in range(2, 15) for suit in 'dchs']
    shuffle(cards)
    return cards

