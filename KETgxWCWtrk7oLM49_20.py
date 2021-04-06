
def tournament_scores(lst):
    teams = set([x for game in lst for x in game if x.isalpha()])
    dic = dict.fromkeys(teams, [0, 0, 0])
    r = []
    for x in lst:
        team1, goal1 , _, goal2, team2 = x.split()
        goal1, goal2 = int(goal1), int(goal2)
        if goal1 > goal2:
            point1, point2 = 3, 0
        elif goal2 > goal1:
            point2, point1 = 3, 0
        else:
            point1, point2 = 1, 1
        dic[team1] = [dic[team1][0] + point1, dic[team1][1] + goal1, dic[team1][2] + (goal1 - goal2)]
        dic[team2] = [dic[team2][0] + point2, dic[team2][1] + goal2, dic[team2][2] + (goal2 - goal1)]
    for x in dic:
        add = [x] + dic[x]
        r.append(add)
    r = sorted(r, key=lambda x : (x[1], x[2], x[3]), reverse=True)
    return r

