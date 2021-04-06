
def over_twenty_one(cards):
  d = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
  return sum(d.get(i, i) for i in cards) > 21

