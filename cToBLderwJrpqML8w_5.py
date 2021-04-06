
def champions(teams):
    max_points = 0
    max_diff = 0
    max_name = ""
    for team in teams:
        points = team["wins"]*3+team["draws"]*1
        diff = team["scored"] - team["conceded"]
        if points>max_points:
            max_name = team["name"]
            max_points = points
            max_diff = diff 
        elif points == max_points:
            if diff>max_diff:
                max_name = team["name"]
                max_points = points
                max_diff = diff
    return max_name

