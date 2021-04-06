
def tower_hanoi(discs):
    count = 0
    if discs == 0:
        return 0
    if discs == 1:
        return 1
    if discs == 2:
        return 3
    count = 1 + tower_hanoi(discs-1) + tower_hanoi(discs-1)
    return count

