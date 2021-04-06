
def dice_roll(n, outcome):
    if n == 1: return 1
    count = 0
    for i in range(1, 7):
        if (n - 1) <= outcome - i <= (n - 1) * 6:
            count += dice_roll(n - 1, outcome - i)
    return count

