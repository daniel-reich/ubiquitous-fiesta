
def is_full_house(hand):
  hand = sorted(hand)
  return ((len(set(hand[:2]))==1 and len(set(hand[2:]))==1) or 
  (len(set(hand[:3]))==1 and len(set(hand[3:]))==1))

