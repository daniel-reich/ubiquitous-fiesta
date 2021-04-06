
def count(deck):
  result=[1 if card in [2,3,4,5,6] else 0 if card in [7,8,9] else -1 for card in deck]
  return sum(result)

