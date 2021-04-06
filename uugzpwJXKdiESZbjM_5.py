
def is_full_house(hand):
  return all([2<=hand.count(x)<=3 for x in hand])

