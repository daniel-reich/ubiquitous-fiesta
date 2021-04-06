
def tournament_scores(tour):
    result = {"A" : ["A", 0, 0, 0], "B" : ["B", 0, 0, 0], "C": ["C", 0, 0, 0], "D" : ["D", 0, 0, 0]}
    for game in tour:
        splittedGame = game.split(" ")
        team1, score1, score2, team2 = splittedGame[0], int(splittedGame[1]), int(splittedGame[-2]), splittedGame[-1]
        if score1 > score2:
            win, lose, points1, points2 = team1, team2, 3, 0
        elif score1 < score2:
            win, lose, points1, points2 = team2, team1, 3, 0
            score1, score2 = score2, score1
        else:
            win, lose, points1, points2 = team1, team2, 1, 1
        result[win][1] += points1
        result[win][2] += score1
        result[win][3] += score1 - score2
        result[lose][1] += points2
        result[lose][2] += score2
        result[lose][3] += score2 - score1 
    output = [team for team in result.values()]
    return sorted(output, key=lambda team : (team[1], team[2], team[3]), reverse=True)

