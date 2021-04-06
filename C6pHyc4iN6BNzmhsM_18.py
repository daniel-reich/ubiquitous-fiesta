
def get_rank(card):
  rank = card[:-1]
  if rank == 'J':
    return 11
  elif rank == 'Q':
    return 12
  elif rank == 'K':
    return 13
  elif rank == 'A':
    return 14
  else:
    return int(rank)
​
def get_ranks(deck):
    ranks = []
    for card in deck:
        rank = get_rank(card)
        if rank not in ranks:
            ranks.append(rank)
    ranks.sort()
    return ranks
def get_suits(deck):
    suits = []
    for card in deck:
        suit = card[-1]
        if suit not in suits:
            suits.append(suit)
    suits.sort()
    return suits
    
def count_rank(deck, rank):
    c = 0
    for card in deck:
        if get_rank(card) == rank:
            c += 1
    return c
​
def poker_hand_ranking(deck):
    ranks = get_ranks(deck)
    suits = get_suits(deck)
    
    is_straight = len(ranks) == len(deck) and ranks[-1] - ranks[0] + 1 == len(ranks)
    is_suit = len(suits) == 1
​
    #check royal flush
    if is_suit and is_straight:
        if ranks[-1] == 14:
            return 'Royal Flush'
        else:
            return 'Straight Flush'
            
    if len(ranks) == 2:
        if count_rank(deck, ranks[0]) == 4 or count_rank(deck, ranks[1]) == 4:
            return 'Four of a Kind'
        return 'Full House'
    if is_suit:
        return 'Flush'
    if is_straight:
        return 'Straight'
        
    if len(ranks) == 3:
        for rank in ranks:
            if count_rank(deck, rank) == 3:
                return 'Three of a Kind'
        return 'Two Pair'
        pair_count = 0
        for rank in ranks:
            if count(deck, rank) == 2:
                pair_count += 1
        if pair_count == 2:
            return 'Two Pair'
        
    if len(ranks) == 4:
        return 'Pair'
    
    return 'High Card'

