
def over_twenty_one(cards):
  d = {'K':10,'Q':10,'J':10, 'A':1}
  return sum([i if isinstance(i, int)==True else d[i] for i in cards])>21

