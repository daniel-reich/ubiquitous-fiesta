
def can_play(hand, face):
  Colors = list(map(lambda Card:Card.split(" ")[0],hand))
  Numbers = list(map(lambda Card:Card.split(" ")[1],hand))
  for Col in range(len(Colors)):
    if Colors[Col] == face.split(" ")[0]:
      return True
  for Num in range(len(Numbers)):
    if Numbers[Num] == face.split(" ")[1]:
      return True
  return False

