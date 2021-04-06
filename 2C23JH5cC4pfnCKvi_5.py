
def check_flush(table, hand):
  suits = [card[-1] for card in table]
  suits_hand = [card[-1] for card in hand]
  for el in suits:
    if suits.count(el) >= 3:
      diff = 5-suits.count(el)
      if suits_hand.count(el) >= diff:
        return True
  return False

