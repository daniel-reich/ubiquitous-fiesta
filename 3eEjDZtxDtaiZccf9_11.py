
def can_play(hand, face):
  
  for card in hand:
    if face[:-2] in card:
      return True
    elif face[-1] == card[-1]:
      return True
      
  return False

