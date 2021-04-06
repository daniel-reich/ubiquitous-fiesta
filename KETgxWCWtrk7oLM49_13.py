
from operator import itemgetter
​
def tournament_scores(lst):
  scored = {}
  taken = {}
  points = {}
​
  for l in lst:
    team1 = l[0]
    goals1 = int(l[2])
    team2 = l[-1]
    goals2 = int(l[-3])
    
    if goals1 > goals2:
      points1 = 3
      points2 = 0
    elif goals1 == goals2:
      points1 = 1
      points2 = 1
    else:
      points1 = 0
      points2 = 3
    
    if team1 in scored.keys():
      scored[team1] = scored[team1] + goals1
      taken[team1] = taken[team1] + goals2
      points[team1] = points[team1] + points1
    else:
      scored[team1] = goals1
      taken[team1] = goals2
      points[team1] = points1
    
    if team2 in scored.keys():
      scored[team2] = scored[team2] + goals2
      taken[team2] = taken[team2] + goals1
      points[team2] = points[team2] + points2
    else:
      scored[team2] = goals2
      taken[team2] = goals1
      points[team2] = points2
  
  result = []
  for key in scored.keys():
    current = []
    current.append(key)
    current.append(int(points[key]))
    current.append(int(scored[key]))
    
    diff = int(scored[key]) - int(taken[key])
    current.append(diff)
    result.append(current)
    
  return sorted(result, key=lambda x: (x[1],x[2],x[3]), reverse=True)

