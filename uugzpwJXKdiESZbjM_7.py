
def is_full_house(hand):
  cards = list(set(hand))
​
  if len(hand) == 5 and len(cards) == 2:
    if hand.count(cards[0]) == 2 or hand.count(cards[1]) == 2:
      return True
  return False

