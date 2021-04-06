
def is_full_house(hand):
  if len(set(hand)) > 2:
    return False
  for card in hand:
    if hand.count(card) > 3:
      return False
  return True

