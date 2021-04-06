
def can_play(hand, face):
  for card in hand:
    if card[:-2] == face[:-2] or card[-1] == face[-1]:
      return True
  return False

