
def poker_hand_ranking(deck):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ranks = sorted([i[:-1] for i in deck], key=order.index)
    flush = len(set(i[-1] for i in deck)) == 1
    group = tuple(sorted([ranks.count(r) for r in set(ranks)], reverse=True))
    straight = len(set(ranks)) == 5 and order.index(ranks[-1]) - order.index(ranks[0]) == 4
​
    if straight and flush:
        return 'Royal Flush' if ranks[-1] == 'A' else 'Straight Flush'
    if straight:
        return 'Straight'
    if flush:
        return 'Flush'
    
    hands = {(4, 1): 'Four of a Kind', 
             (3, 2): 'Full House', 
             (3, 1, 1): 'Three of a Kind',
             (2, 2, 1): 'Two Pair', 
             (2, 1, 1, 1): 'Pair', 
             (1, 1, 1, 1, 1): 'High Card'}
    
    return hands[group]

