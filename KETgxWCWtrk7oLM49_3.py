
from operator import itemgetter
​
​
def add_scores(teams):
​
    for team_data in teams:
​
        if team_data[0] == "A":
​
            a[1] += team_data[1]
            a[2] += team_data[2]
            a[3] += team_data[3]
​
        elif team_data[0] == "B":
​
            b[1] += team_data[1]
            b[2] += team_data[2]
            b[3] += team_data[3]
​
        elif team_data[0] == "C":
​
            c[1] += team_data[1]
            c[2] += team_data[2]
            c[3] += team_data[3]
​
        elif team_data[0] == "D":
​
            d[1] += team_data[1]
            d[2] += team_data[2]
            d[3] += team_data[3]
​
​
def tournament_scores(lst):
​
    global a, b, c, d
    a = ["A", 0, 0, 0]
    b = ["B", 0, 0, 0]
    c = ["C", 0, 0, 0]
    d = ["D", 0, 0, 0]
​
    for math in lst:
​
        every_team_data = math.split(" - ")
​
        team_one_name = every_team_data[0].split(" ")[0]
        team_two_name = every_team_data[1].split(" ")[1]
        team_one_goals = int(every_team_data[0][-1])
        team_two_goals = int(every_team_data[1][0])
​
        goal_differnce_one = team_one_goals - team_two_goals
        goal_differnce_two = team_two_goals - team_one_goals
​
        if team_one_goals == team_two_goals:
​
            add_scores(((team_one_name, 1, team_one_goals, goal_differnce_one),
                        (team_two_name, 1, team_two_goals, goal_differnce_two)))
​
        elif team_one_goals > team_two_goals:
​
            add_scores(((team_one_name, 3, team_one_goals, goal_differnce_one),
                        (team_two_name, 0, team_two_goals, goal_differnce_two)))
​
        elif team_one_goals < team_two_goals:
​
            add_scores(((team_one_name, 0, team_one_goals, goal_differnce_one),
                        (team_two_name, 3, team_two_goals, goal_differnce_two)))
​
    results = [a, b, c, d]
    results = sorted(results, key=itemgetter(1, 2, 3))
    results.reverse()
​
    return results

