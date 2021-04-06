
def dice_game(scores):
    players = ['p1', 'p2', 'p3', 'p4']
​
    def remve_player(player_index):
        nonlocal scores
        scores = scores[len(players):]
        players.pop(player_index)
​
    while len(players) > 1:
        total_scores = [sum(s) for s in scores[:len(players)]]
        min_score = min(total_scores)
        min_count = total_scores.count(min_score)
        if min_count == 1:
            remve_player(total_scores.index(min_score))
        else:
            first_dice_score = [s[0] for s in scores[:len(players)]]
            min_score = min(first_dice_score)
            min_count = first_dice_score.count(min_score)
            if min_count == 1:
                remve_player(first_dice_score.index(min_score))
            else:
                scores = scores[len(players):]
    return players[0]

