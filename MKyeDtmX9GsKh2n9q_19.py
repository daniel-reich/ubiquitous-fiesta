
def gen_deck():
  suits = ('c', 'd', 's', 'h')
  cards = (i for i in range(2, 15))
  deck = []
  for card in cards:
    for suit in suits:
      deck.append((card, suit))
  return deck

