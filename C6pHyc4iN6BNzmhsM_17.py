
def consecutive_difs(lst):
  difs = []
  for i in range(1, len(lst)):
    difs.append( lst[i] - lst[i-1] )
  return difs
  
def counter(lst):
  counts = []
  for item in lst:
    counts.append(lst.count(item))
  return counts
​
def poker_hand_ranking(hand):
  ranks = []
  suits = []
  face_cards = {'A':14, 'K':13, 'Q':12, 'J':11}
  for card in hand:
    suits.append( card[-1] )
    try:
      ranks.append( int(card[:-1]) )
    except ValueError:
      ranks.append( face_cards[ card[:-1] ] )
      
  if len(set(suits)) == 1:    # have some type of flush
    if consecutive_difs( sorted(ranks) ) == [1, 1, 1, 1]:
      if max(ranks) == 14:
        return 'Royal Flush'
      else:
        return 'Straight Flush'
    else:
      return 'Flush'
      
  elif consecutive_difs( sorted(ranks) ) == [1, 1, 1, 1]:
    return 'Straight'
    
  else:
    if sorted( counter(ranks) ) == [1, 4, 4, 4, 4]:
      return 'Four of a Kind'
    elif sorted( counter(ranks) ) == [2, 2, 3, 3, 3]:
      return 'Full House'
    elif sorted( counter(ranks) ) == [1, 1, 3, 3, 3]:
      return 'Three of a Kind'
    elif sorted( counter(ranks) ) == [1, 2, 2, 2, 2]:
      return 'Two Pair'
    elif sorted( counter(ranks) ) == [1, 1, 1, 2, 2]:
      return 'Pair'
    else:
      return 'High Card'

