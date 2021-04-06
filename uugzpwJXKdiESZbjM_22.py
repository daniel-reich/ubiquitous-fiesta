
def is_full_house(hand):
  dict = {}
  for c in hand:
    if c not in dict:
      dict[c] = 1
    else:
      dict[c] += 1
  if 3 in dict.values() and 2 in dict.values():
    return True
  else:
    return False

