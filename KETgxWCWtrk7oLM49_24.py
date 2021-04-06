
def tournament_scores(matches):
    points = {}
    goals = {}
    nets = {}
​
    for match in matches:
       p = match.split(" ")
       r = p.copy()
       r.reverse()
       for teamA, goalA, _, goalB, teamB in [p, r]:
           points[teamA] = points.get(teamA, 0) + 3 * (goalA > goalB)
           points[teamA] = points.get(teamA, 0) + 1 * (goalA == goalB)
           goals[teamA] = goals.get(teamA, 0) + int(goalA)
           nets[teamA] = nets.get(teamA, 0) + int(goalA) - int(goalB)
    scores = [[team, points[team], goals[team], nets[team]] for team in \
             points.keys()]
    return sorted(scores, key=lambda e: (e[1], e[2], e[3]), reverse=True)

