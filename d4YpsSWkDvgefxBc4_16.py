
def over_twenty_one(cards):
  x = sum([10 if cards[i] == "J" or cards[i] == "Q" or cards[i] == "K" else 1 if cards[i] == "A" else cards[i] for i in range(0, len(cards))])
  if x <= 11 and "A" in cards:
    x += 10
  return x>21

