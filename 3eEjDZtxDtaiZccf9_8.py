
def can_play(hand, face):
  return face.split()[0] in [j for i in hand for j in i.split() if not j.isdigit()] or face.split()[1] in [j for i in hand for j in i.split() if j.isdigit()]

