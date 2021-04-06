
def can_play(hand, face):
  for i in hand:
    if i.split()[0] == face.split()[0] or i.split()[1] == face.split()[1]:
      return True
  return False

