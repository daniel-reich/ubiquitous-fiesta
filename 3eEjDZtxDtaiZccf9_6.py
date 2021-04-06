
def can_play(hand, face):
  for card in hand:
    for part in card.split():
      if part in face:
        return True
  return False

