
def check_flush(table, hand):
  d = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
  for card in table:
    d[card[-1]] += 1
  for card in hand:
    d[card[-1]] += 1
  for key in d.keys():
    if d[key] >= 5:
      return True
  return False

