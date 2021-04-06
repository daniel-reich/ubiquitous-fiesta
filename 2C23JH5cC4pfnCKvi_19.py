
def check_flush(table, hand):
    table_suit = [i[-1] for i in table]
    hand_suit = [i[-1] for i in hand]
    if len(set(hand_suit)) == 2:
        return False
    else:
        suit = hand[0][-1]
        return table_suit.count(suit) >= 3

