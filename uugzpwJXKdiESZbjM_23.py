
def is_full_house(hand):
  list1=list(set(hand))
  if len(list1)!=2:
    return False
  else:
    return hand.count(list1[0])==2 or hand.count(list1[0])==3

