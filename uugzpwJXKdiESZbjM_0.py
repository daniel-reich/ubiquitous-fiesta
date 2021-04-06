
def is_full_house(hand):
  return all(hand.count(i) >= 2 for i in hand)

