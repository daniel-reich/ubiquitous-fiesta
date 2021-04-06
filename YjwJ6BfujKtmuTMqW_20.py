
def dice_game(*die):
    all_dices = (die[0])
    players = ["p1", "p2", "p3", "p4"]
    while len(players) > 1:
        dice_dict = {}
        for i in range(len(players)):
            dice_dict[players[i]] = all_dices[i]
        all_dices = all_dices[len(players):]
        dice_sum_dict = {}
        for player in dice_dict:
            dice_sum_dict[player] = dice_dict[player][0] + dice_dict[player][1]
        min_dice = min(dice_sum_dict.values())
        same_score = {}
        for player in dice_sum_dict:
            if dice_sum_dict[player] == min_dice:
                same_score[player] = dice_dict[player][0]
        min_1st_dice = min(same_score.values())
        min_count = 0
        for player in same_score:
            if same_score[player] == min_1st_dice:
                loser = player
                min_count += 1
        if min_count == 1:
            players.remove(loser)
    winner = players[0]
    return (winner)

