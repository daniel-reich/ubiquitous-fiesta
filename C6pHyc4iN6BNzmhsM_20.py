
def poker_hand_ranking(hand):
  print(hand)
  k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  d = {'A': 0, 'K': 13, 'Q': 12, 'J': 11}
​
  suits = [card[-1] for card in hand]
  values = [card[:-1] for card in hand]
  values_ = [d[card] if card in 'KQJA' else int(card) for card in values]
  count = sum(map(values.count, values))
  
  full = count == 13
  four = count == 17
  three = count == 11
  two = count == 9
  one = count == 7
  flush = suits.count(suits[0]) == 5
  
  a = k.index(min(values_))
  b = k.index(max(values_))
  straight = b - a == 4
  print(values_)
  print(straight, b, a)
  r = [0, 11, 10, 12, 13]
  royal = [x in r for x in values_]
  r2 = [10, 11, 12, 13, 0]
  st2 = True
  for x in values_:
    if x not in r2:
      st2 = False
      break
      
  
  if flush:
    if all(royal):
      return 'Royal Flush'
    elif straight:
      return 'Straight Flush'
    else:
      return 'Flush'
  if four: return 'Four of a Kind'
  
  if full: return 'Full House'
​
  if straight or st2: return 'Straight'
​
  if three: return 'Three of a Kind'
​
  if two: return 'Two Pair'
​
  if one: return 'Pair'
​
  return 'High Card'

