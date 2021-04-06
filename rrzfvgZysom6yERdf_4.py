
card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
​
def hand_rank(hand):
    a = sorted([i[0] for i in hand])
    
    #Royal Flush
    if a == sorted(["A", "K", "Q", "J", "T"]) and len(set(i[1] for i in hand)) == 1:
        return (10, )
    
    #Straight Flush
    elif a == sorted(card_ranks[card_ranks.index(a[0]):card_ranks.index(a[0]) + 5]) and len(set(i[1] for i in hand)) == 1:
        return (9, )
    elif len(set(a)) == 2:
        
        #Four of a Kind
        if 4 in [a.count(i) for i in a]:
            return (8, card_ranks.index([i for i in a if a.count(i) == 4][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 4], reverse = True))
        
        #Full House
        else:
            return (7, card_ranks.index([i for i in a if a.count(i) == 3][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 3], reverse = True))
    
    #Flush
    elif len(set(i[1] for i in hand)) == 1:
        return (6, )
    
    #Straight
    elif a == sorted(card_ranks[card_ranks.index(a[0]):card_ranks.index(a[0]) + 5]):
        return (5, )
    elif len(set(a)) == 3:
        
        #Three of a Kind
        if sorted([a.count(i) for i in a]) == [1, 1, 3, 3, 3]:
            return (4, card_ranks.index([i for i in a if a.count(i) == 3][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 3], reverse = True))
        
        #Two Pairs
        else:
            return (3, card_ranks.index([i for i in a if a.count(i) == 2][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 2], reverse = True))
    
    #One Pair
    elif sorted([a.count(i) for i in a]) == [1, 1, 1, 2, 2]:
        return (2, card_ranks.index([i for i in a if a.count(i) == 2][0]), sorted([card_ranks.index(i) for i in a if a.count(i) != 2], reverse = True))
    
    #High Card
    else:
        b = sorted([card_ranks.index(i) for i in a], reverse = True)
        b.remove(max(card_ranks.index(i) for i in a))
        return (1, max(card_ranks.index(i) for i in a), b)
​
​
def winner(pl1, pl2):
    if hand_rank(pl1)[0] > hand_rank(pl2)[0]:
        return "Player1"
    elif hand_rank(pl1)[0] < hand_rank(pl2)[0]:
        return "Player2"
    else:
        if hand_rank(pl1)[1] > hand_rank(pl2)[1]:
            return "Player1"
        elif hand_rank(pl1)[1] < hand_rank(pl2)[1]:
            return "Player2"
        else:
            for i in range(5):
                if hand_rank(pl1)[2][i] > hand_rank(pl2)[2][i]:
                    return "Player1"
                elif hand_rank(pl1)[2][i] < hand_rank(pl2)[2][i]:
                    return "Player2"
                else:
                    continue
​
def player1_wins(lst):
    c = 0
    for i in lst:
        p1 = i.split(" ")[:5]
        p2 = i.split(" ")[5:]
        if winner(p1, p2) == "Player1":
            c += 1
    return c

