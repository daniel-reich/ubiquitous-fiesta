
def check_flush(table, hand):
  all_cards = table + hand
  suits = []
  for card in all_cards:
    suits.append(card[-1])
  for letter in suits:
    if suits.count(letter) > 4.5:
      return True
  return False

