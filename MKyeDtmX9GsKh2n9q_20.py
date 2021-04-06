
def gen_deck():
  suits = ['d','c','s','h']
  faces = list(range(2,15))
  deck = []
  for i in suits:
    for j in faces:
      deck.append((j,i))
  return deck

