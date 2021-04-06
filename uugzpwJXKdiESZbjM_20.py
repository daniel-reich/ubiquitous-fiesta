
def is_full_house(hand):
  s=set(hand)
  if len(s)==2:
    x=hand.count(s.pop())
    if x==3 or x==2: return True
  return False

