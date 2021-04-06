
def is_full_house(hand):
  x = []
  for i in hand:
    if hand.count(i) < 3:
      if hand.count(i) < 2:
        return False
      else:
        return True

