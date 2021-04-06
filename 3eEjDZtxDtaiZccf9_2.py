
def can_play(hand, face):
  return any(x[:-1] == face[:-1] or x[-1] == face[-1] for x in hand)

