
from collections import Counter
def poker_hand_value(hand):
    rank = 1 
    order = 'AKQJT98765432'
    card_counts = sorted(Counter([c[:-1] for c in hand]).most_common(5), key=lambda c: (-c[1], order.index(c[0]))) # list of tuple (card value, count)
    card_seq = sorted(order.index(c[0]) for c in hand) # list in order 0 = A, 1 = J, 2 = Q, .... 2 = 12
    suit_counts = list(Counter([c[-1] for c in hand]).items()) # list of tuple (suit, count) in descending order of count
    is_straight = all(card_seq[i+1] - card_seq[i] == 1 for i in range(4))
    if len(suit_counts) == 1: # it's a flush
        if is_straight:
            rank = 10 if card_seq[0] == 0 else 9
        else:
           rank = 6
    elif is_straight: rank = 5
    elif card_counts[0][1] == 4: rank = 8
    elif card_counts[0][1] == 3:
        rank = 7 if card_counts[1][1] == 2 else 4
    elif card_counts[0][1] == 2:
        rank = 3 if card_counts[1][1] == 2 else 2
    discr = sum(13**(5-i)*(13 - order.index(c[0])) for i, c in enumerate(card_counts))
    return (rank, discr)
​
def player1_wins(lst):
    wins = 0
    for hands in lst:
        cards = hands.split()
        r1 = poker_hand_value(cards[:5])
        r2 = poker_hand_value(cards[5:])
        if r1 > r2:
            wins += 1
    return wins

