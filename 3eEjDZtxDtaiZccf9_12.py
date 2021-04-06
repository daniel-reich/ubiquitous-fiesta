
def can_play(hand, face):
  lst = [elem.split() for elem in hand]
  for elem in lst: 
    if elem[0] == face.split()[0] or int(elem[1]) == int(face.split()[1]):
      return True
  return False

