
def player1_wins(lst):
    '''
    Returns a count of the number of times player1 wins for each pair of hands
    in lst, as per the rules of poker outlined in the instructions
    '''
    from collections import Counter
​
    RANKS = ('AKQJT98765432')
    VALUES = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    
    value = lambda x: VALUES[x[0]] if x[0] in VALUES else int(x[0]) # single card
​
    is_flush = lambda x: all(x[i][1] == x[0][1] for i in range(1,5))
​
    is_straight = lambda x: all(value(x[i][0]) == value(x[i-1][0]) - 1
                                for i in range(1,5)) 
    
    highest = lambda x,y=None: value(x[0])
​
    straight_flush = lambda x,y: 180 + value(x[0]) if (is_straight(x) and is_flush(x))\
                     else 0  # automatically scores royal flush higher
​
    four_kind = lambda x,y: 160 + value(y[0][1]) if y[0][0] == 4 else 0
​
    full_house = lambda x,y: 140 + value(y[0][1]) if (y[0][0] == 3 and y[0][1] == 2) \
                 else 0
                 
    three_kind = lambda x,y: 80 + value(y[0][1]) if y[0][0] == 3 else 0
​
    two_pairs = lambda x,y: 60 + value(y[0][1]) if (y[0][0] == 2 and y[0][1] == 2) \
                 else 0
​
    one_pair = lambda x,y: 40 + value(y[0][1]) if y[0][0] == 2 else 0
​
    straight = lambda x,y: 100 if is_straight(x) else 0
​
    flush = lambda x,y: 120 if is_flush(x) else 0
​
    hand_checks = (straight_flush, four_kind, flush, straight,
                   three_kind, two_pairs, one_pair, highest) # check in this order
    scores = [0,0]  # score each hand
​
    count = 0
    for hands in lst:
        hands = hands.split()
        p1 = sorted([hands[i] for i in range(5)],
                         key=lambda x: RANKS.index(x[0]))
        p2 = sorted([hands[i] for i in range(5,10)],
                         key=lambda x: RANKS.index(x[0]))
        dealt = (p1, p2)
        values = []
        
        for i in range(len(scores)):
            ranks = ''.join(c[0] for c in dealt[i])
            values.append(sorted(set([(ranks.count(s),s) for s in ranks]), reverse=True))  # for use in n of a kind checks
            
            for check in hand_checks:
                score = check(dealt[i], values[i])
                if score:
                    scores[i] = score
                    break
​
        if scores[0] > scores[1]: # p1 won
            count += 1
        elif scores[0] == scores[1]:  # same - need highest
            for i in range(len(values[0])):
                p1v, p2v = value(values[0][i][1]), value(values[1][i][1])
                if p1v == p2v:
                    continue
                if p1v > p2v:  # p1 wins tie-breaker
                    count += 1
                break
​
    return count

