
def gen_deck():
  deck = []
  for i in range(2, 15):
    deck.append((i, 'd'))
    deck.append((i, 's'))
    deck.append((i, 'c'))
    deck.append((i, 'h'))
  return deck

