
def dice_game(scores):
    players = ["p1", "p2", "p3", "p4"]
    while len(players) > 1:
        L = []
        for p in players:
            d1, d2 = scores.pop(0)
            L.append([p, d1 + d2, d1])
        L.sort(key=lambda x: (-x[1], -x[2]))
        if L[-2][1] > L[-1][1]:
            # one player has unique lowest total and is eliminated:
            players.remove(L[-1][0])
        elif L[-2][2] > L[-1][2]:
            # tie for lowest total but unique first rolls:
            players.remove(L[-1][0])   
    return players[0]

