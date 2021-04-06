
def is_full_house(hand):
  counts = [hand.count(i) for i in set(hand)]
  if 3 in counts and 2 in counts:
    return True
  else: return False

