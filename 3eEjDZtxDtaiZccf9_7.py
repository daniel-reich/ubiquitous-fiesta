
def can_play(hand, face):
  a=[x.split(' ') for x in hand]
  b=face.split(' ')
  for i in a:
    if i[0] in b or i[1] in b: return True
  return False

