
def check_flush(table, hand):
  table += hand
​
  table = [card[-1] for card in table]
  for suit in table:
    if table.count(suit) >= 5:
      return True
  return False

