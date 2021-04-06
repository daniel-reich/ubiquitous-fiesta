
def dice_game(scores):
    players = [1, 2, 3, 4]
    while len(players) > 1:
        low_roll1 = 0
        low_roll2 = 0
        low_player = 0
        for player in players:
            roll1, roll2 = scores.pop(0)
            if player == min(players):
                low_roll1 = roll1
                low_roll2 = roll2
                low_player = player
            elif roll1 + roll2 < low_roll1 + low_roll2:
                low_roll1 = roll1
                low_roll2 = roll2
                low_player = player
            elif roll1 + roll2 == low_roll1 + low_roll2:
                if roll1 < low_roll1:
                    low_roll1 = roll1
                    low_roll2 = roll2
                    low_player = player
                elif roll1 == low_roll1:
                    low_player = 0
        if  low_player != 0:
            players.remove(low_player)
    return 'p' + str(players[0])

