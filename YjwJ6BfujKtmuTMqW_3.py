
def dice_game(scores):
    players, dice = [1, 2, 3, 4], [(0, 0), (0, 0), (0, 0), (0, 0)]
​
    def remove_player(d, p):
        game = sorted(zip(p, d, [sum(d) for d in d]), key=lambda x: x[2])
        if game[0][2] == game[1][2]:
            game = sorted(zip(p, d, [sum(d) for d in d]), key=lambda x: (x[2], x[1][0]))
            return 0 if game[0][1][0] == game[1][1][0] else game[0][0]
        else:
            return game[0][0]
​
    while len(scores) > 0:
        if len(scores) < len(players):
            pass
        for i in range(0, len(players)):
            dice[i] = scores[0]
            del scores[0]
        dups = remove_player(dice, players)
        if dups > 0:
            players.remove(dups)
        else:
            pass
    return 'p%s' %(int(players[0]))

