
def poker_hand_ranking(hand):
    lookup = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "1":10, "J":11, "Q":12, "K":13, "A":14}
    values = []
    suits = []
    for x in range(len(hand)):
        values.append(lookup.get(hand[x][0]))
        suits.append(hand[x][len(hand[x]) - 1])
    values.sort()
    
    #royal/straight/flush
    if suits.count(suits[0]) == len(suits):
        if values == list(range(min(values), max(values) + 1)):
            if values == list(range(10, 15)):
                return "Royal Flush"
            return "Straight Flush"
        return "Flush"
    
    #four of a kind
    if values.count(values[0]) == 4 or values.count(values[1]) == 4:
        return "Four of a Kind"
    
    #full house/three of a kind
    if values.count(values[1]) == 3:
        if values.count(values[len(values) - 1]) == 2:
            return "Full House"
        return "Three of a Kind"
    if values.count(values[len(values) - 1]) == 3:
        if values.count(values[1]) == 2:
            return "Full House"
        return "Three of a Kind"
    
    #straight
    if values == list(range(min(values), max(values) + 1)):
        return "Straight"
    
    #two pair
    if values.count(values[1]) == 2:
        if values.count(values[3]) == 2:
            return "Two Pair"
        return "Pair"
    if values.count(values[3]) == 2:
        if values.count(values[1]) == 2:
            return "Two Pair"
        return "Pair"
    
    return "High Card"

