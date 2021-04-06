
def champions(teams):
    L = []
    for d in teams:
        name = d["name"]
        points = 3 * d["wins"] + d["draws"]
        goal_diff = d["scored"] - d["conceded"]
        L.append([name, points, goal_diff])
    L.sort(key=lambda x: (-x[1], -x[2]))
    return L[0][0]

