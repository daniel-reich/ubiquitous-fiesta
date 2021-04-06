
def dice_game(lst):
    score = 0
    for dice_result in lst:
        if len(set(dice_result)) == 1:
            return 0
        score += sum(dice_result)
    return score

