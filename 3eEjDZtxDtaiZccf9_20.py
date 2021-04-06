
def can_play(hand, face):
  for card in hand:
    if card.split(" ")[0] in face or \
      card.split(" ")[1] in face:
      return True
  return False

