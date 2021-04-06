
def dice_game(lst):
    sum = 0
    for rolls in lst:
        if rolls[0] == rolls[1]:
            return 0
        else:
            sum += rolls[0]+rolls[1]
    return sum

