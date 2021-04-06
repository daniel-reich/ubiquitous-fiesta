
def gen_deck():
  deck = []
  for i in ['s','h','d','c']:
    for j in range(2,15):
      deck.append((j,i))
  return deck[5:]+deck[:5]

