
def dice_game(scores):
    players = list(range(4))
    while len(players) > 1:
        game_round, scores = scores[:len(players)], scores[len(players):]
        _round = []
        for i in range(len(game_round)):
            _round += [[game_round[i], players[i]]]
        _round.sort(key=lambda x: (x[0][0] + x[0][1], x[0]))
        if sum(_round[0][0]) < sum(_round[1][0]) \
                or _round[0][0][0] < _round[1][0][0]:
            players = players[:players.index(_round[0][1])] \
                      + players[players.index(_round[0][1]) + 1:]
    return 'p' + str(players[0] + 1)

