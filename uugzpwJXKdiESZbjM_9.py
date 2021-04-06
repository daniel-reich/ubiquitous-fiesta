
def is_full_house(hand):
  counts = {}
  for card in hand:
    counts[card] = counts.get(card, 0) + 1
  threes = sum([1 for cnt in counts.values() if cnt == 3])
  twos = sum([1 for cnt in counts.values() if cnt == 2])
  return threes == 1 and twos == 1

