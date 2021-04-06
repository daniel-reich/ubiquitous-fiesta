
def can_play(hand, face):
  atts = sum([x.split() for x in hand],[])
  return any([x in face.split() for x in atts])

