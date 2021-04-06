
def check_flush(table, hand):
  suits = [c[-1] for c in table + hand]
  return any(suits.count(s) > 4 for s in set(suits))

