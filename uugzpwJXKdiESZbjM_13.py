
def is_full_house(hand):
  lst = []
  for i in hand:
    if hand.count(i) != 3 and hand.count(i) != 2:
      return False
  return True

