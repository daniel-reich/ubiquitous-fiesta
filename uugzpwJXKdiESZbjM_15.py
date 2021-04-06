
def is_full_house(hand):
  return len(set(hand)) == 2  and ( hand.count(hand[0]) == 2 or hand.count(hand[0]) == 3);

