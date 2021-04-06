
def tournament_scores(lst):
  teams = { char: [char, 0, 0, 0] for char in 'ABCD' }
  for match in lst:
    [teamA, scoreA], [scoreB, teamB] = match.replace(' ', '').split('-')
    scoreA, scoreB = int(scoreA), int(scoreB)
    
    teams[teamA][1] += calculate_score(scoreA, scoreB)
    teams[teamA][2] += scoreA
    teams[teamA][3] += scoreA - scoreB
    
    teams[teamB][1] += calculate_score(scoreB, scoreA)
    teams[teamB][2] += scoreB
    teams[teamB][3] += scoreB - scoreA
    
  results = [team_data for team, team_data in teams.items()]
  results.sort(key=lambda l: (l[1], l[2], l[3]), reverse=True)
  return results
    
def calculate_score(our_score, other_score):
  if our_score > other_score:
    return 3
  if our_score < other_score:
    return 0
  return 1

