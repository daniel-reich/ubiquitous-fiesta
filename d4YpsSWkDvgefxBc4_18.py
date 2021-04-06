
def over_twenty_one(cards):
  return sum([i if isinstance(i, int) else 1 if i == 'A' else 10 for i in cards]) > 21

