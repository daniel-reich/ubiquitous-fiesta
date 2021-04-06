
def count(deck):
  count = 0
  for card in deck:
    if card in [2, 3, 4, 5, 6]:
      count += 1
    if card in [10, "J", "Q", "K", "A"]:
      count -= 1
  return count

