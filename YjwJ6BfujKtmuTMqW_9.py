
def dice_game(scores):
    rest_scores = [sum(x)*10+x[0] for x in scores]
    rest_players=['p1','p2','p3','p4']
    while len(rest_players)>1:
        s = sorted(zip(rest_scores, rest_players))
        rest_scores = rest_scores[len(rest_players):]
        if s[0][0]<s[1][0]:
            rest_players.remove(s[0][1])
    return rest_players[0]

