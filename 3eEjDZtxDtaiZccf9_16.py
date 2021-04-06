
def can_play(hand, face):
  face = face.split()
  hand = list(x.split() for x in hand)
  for x in hand:
    if x[0] == face[0] or x[1] == face[1]:
      return True
  return False

