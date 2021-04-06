
def is_full_house(hand):
  hand = sorted(hand)
  if (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]) or (
  hand[0] == hand[1] == hand[2] and hand[3] == hand[4]):
    return True
  else:
    return False

