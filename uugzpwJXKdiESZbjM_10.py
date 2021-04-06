
def is_full_house(hand):
  return len(set(hand))==2 and (hand.count(sorted(hand)[0])==3 and hand.count(sorted(hand)[-1])==2) or (hand.count(sorted(hand)[0])==2 and hand.count(sorted(hand)[-1])==3)

