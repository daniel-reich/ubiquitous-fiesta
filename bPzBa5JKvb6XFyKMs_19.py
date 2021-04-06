
def get_primiera_score(deck):
  key = {'7': 21, '6': 18, 'A': 16, '5': 15, '4': 14, '3': 13,
       '2': 12, 'J': 10, 'Q': 10, 'K': 10}
  suits = {'c': 0, 'd': 0, 'h': 0, 's': 0}
  for c in deck:
    suits[c[1]] = max(suits[c[1]], key[c[0]])
  return 0 if 0 in suits.values() else sum(suits.values())

