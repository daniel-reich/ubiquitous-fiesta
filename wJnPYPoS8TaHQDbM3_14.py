
def dice_roll(dices, n):
    if dices == 1:
        return 1 <= n <= 6
    return sum(dice_roll(dices -1, n -i) for i in range(1, min(6, n) +1))

