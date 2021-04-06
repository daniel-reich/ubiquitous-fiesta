
def is_full_house(hand):
    if (len(set(hand))) == 2 and sorted(hand).count(hand[0]) == 2 or sorted(hand).count(hand[0]) == 3 :
        return True
    else:
        return False

