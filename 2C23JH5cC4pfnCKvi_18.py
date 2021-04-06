
def check_flush(table, hand):
    hand_suit = hand[0][-1]
    count = 0
    for s in table:
        if s[-1] == hand_suit:
            count += 1
    return True if count >= 3 else False

