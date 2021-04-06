
def is_full_house(hand):
  return True if [i for i in hand if hand.count(i) == 3] else False

