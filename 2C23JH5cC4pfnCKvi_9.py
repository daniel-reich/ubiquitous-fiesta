
def check_flush(table, hand):
  combined = table + hand
  suit_count = {}
  
  for card in combined:
    suit = card[-1]
    if suit not in suit_count:
      suit_count[suit] = 1
    else:
      suit_count[suit] += 1
  
  max_count = max([count for count in suit_count.values()])
  
  return max_count >= 5

