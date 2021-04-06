
def check_flush(table, hand):
​
    card_one_flush = []
​
    for i in table:
        if i.endswith(hand[0][-1]):
            card_one_flush.append(i)
    for i in hand:
        if i.endswith(card_one_flush[0][-1]):
            card_one_flush.append(i)
    
    card_two_flush = []
    for i in table:
        if i.endswith(hand[1][-1]):
            card_two_flush.append(i)
    for i in hand:
        if i.endswith(card_two_flush[0][-1]):
            card_two_flush.append(i)
​
    return len(card_one_flush) >= 5 or len(card_two_flush) >= 5

