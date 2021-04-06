
def can_play(hand, face):
  for x in hand:
    if x.split()[0]==face.split()[0] or x.split()[1]==face.split()[1]:
      return True
  return False

