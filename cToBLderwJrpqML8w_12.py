
def champions(teams):
    points = []
    for i in teams:
        points.append(3*i["wins"]+1*i["draws"])
    points = sorted(points)[::-1]
    if points[0] != points[1]:
        for i in teams:
            if points[0] == 3*i["wins"]+1*i["draws"]:
                return i["name"]
    else:
        score = []
        for i in teams:
            if points[0] == 3*i["wins"]+1*i["draws"]:
                score.append(i["scored"]-i["conceded"])
        score = sorted(score)[::-1]
        for i in teams:
            if score[0] == i["scored"]-i["conceded"]:
                return i["name"]

