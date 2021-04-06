
def can_play(hand, face):
  return any([y in face for x in hand for y in x.split()])

