
def can_play(hand, face):
  handsplit = [elem for sublist in [item.split() for item in hand] for elem in sublist]
  return (face.split()[0] in handsplit or face.split()[1] in handsplit)

