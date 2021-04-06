
def dice_game(scores):
    players = ['p1', 'p2', 'p3', 'p4']
    
    while len(players) > 1:
        results = list(zip(players, scores))
        scores = scores[len(players):]
        results.sort(key=lambda x: (sum(x[1]), x[1][0]))
        if results[0][1] != results[1][1]:
            players.remove(results[0][0])
    return players[0]

