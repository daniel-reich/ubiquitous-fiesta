
def lemonade(bills):
    hand = {v: 0 for v in [5, 10, 20]}
    for bill in bills:
        if bill == 5:
            hand[5] += 1
        elif bill == 10:
            if hand[5] > 0:
                hand[5] -= 1
            else:
                return False
            hand[10] += 1
        else:   # bill = 20
            if hand[5] > 0 and hand[10] > 0:
                hand[5] -= 1
                hand[10] -= 1
            elif hand[5] >= 3:
                hand[5] -= 3
            else:
                return False
            hand[20] += 1
    return True

