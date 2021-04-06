
def can_play(hand, face):
  brokenface = face.split(' ')
  for ele in hand:
    brokenhand=ele.split(' ')
    if brokenface[0] in brokenhand[0]:
      return True
    elif brokenface[1] in brokenhand[1]:
      return True
  return False

