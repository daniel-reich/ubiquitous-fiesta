
def poker_hand_ranking(hand):
  d = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  
  values = sorted(int(d.get(i[:-1], i[:-1])) for i in hand)
  suits = len(set(i[-1] for i in hand))
  
  if suits == 1 and values == list(range(10, 15)):
    return 'Royal Flush'
  if suits == 1 and values == list(range(min(values),max(values)+1)):
    return 'Straight Flush'
  if any(values.count(i) == 4 for i in values):
    return 'Four of a Kind'
  if len(set(values)) == 2:
    return 'Full House'
  if suits == 1:
    return 'Flush'
  if values == list(range(min(values),max(values)+1)):
    return 'Straight'
  if any(values.count(i) == 3 for i in values):
    return 'Three of a Kind'
  if len(set(values)) == 3:
    return 'Two Pair'
  if len(set(values)) == 4:
    return 'Pair'
  return 'High Card';

