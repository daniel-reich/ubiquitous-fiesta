
def is_full_house(hand):
  return sorted(hand.count(card) for card in set(hand)) == [2, 3]

