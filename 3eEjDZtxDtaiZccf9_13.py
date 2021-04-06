
def can_play(hand, face):
  new_face = face.split()
  for i in hand:
    first=i.split()
    if first[0]==new_face[0] or first[1]==new_face[1] :
      return True
  return False

