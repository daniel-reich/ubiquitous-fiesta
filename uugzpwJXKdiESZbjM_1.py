
def is_full_house(hand):
  return set([hand.count(i) for i in hand]) == {3, 2}

