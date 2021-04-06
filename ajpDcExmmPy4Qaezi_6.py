
class League:
  class Team:
​
    def __init__(self, name, played, won, drawn, lost, g_diff):
      self.name = name
      self.play = played
      self.won = won
      self.draw = drawn
      self.lost = lost
      self.gdif = g_diff
​
      self.points = (self.won * 3) + self.draw
    
    def __lt__(self, other):
​
      if self.points != other.points:
        return self.points < other.points
      else:
        return self.gdif < other.gdif
    
    def __gt__(self, other):
      if self.points != other.points:
        return self.points > other.points
      else:
        return self.gdif > other.gdif
    
    def data(self):
      return [self.name, self.points, self.gdif]
  
  def __init__(self, league):
​
    self.l = league
    self.teams = {}
​
    for lst in league:
      name, games, won, drawn, lost, gd = lst
      team = League.Team(name, games, won, drawn, lost, gd)
      self.teams[name] = team
  
  def find_winner(teams, tid):
    team = teams[tid]
    for ti in teams.keys():
      if ti != tid:
        if team < teams[ti]:
          return League.find_winner(teams, ti)
    return tid
  
  def find_loser(teams, tid):
    try:
      team = teams[tid]
    except TypeError:
      print(teams, tid)
      return 'hjlks'
    for ti in teams.keys():
      if ti != tid:
        if team > teams[ti]:
          return League.find_loser(teams, ti)
    return tid
  
  def sort_teams(dict, teams):
    if len(teams) == 0:
      return []
    elif len(teams) == 1:
      return [teams[0]]
    else:
     # print(teams)
      loser = League.find_loser(dict, teams[0])
      winner = League.find_winner(dict, teams[0])
      try:
        teams.pop(teams.index(loser))
        teams.pop(teams.index(winner))
        nd = {key: dict[key] for key in dict.keys() if key not in [loser, winner]}
      except ValueError:
        print('Loser: {}\nWinner: {}\nTeams: {}'.format(loser, winner, teams),'Norwich' in teams)
        return []
      return [loser] + League.sort_teams(nd, teams) + [winner]
​
  def find_team_place(self, team):
    sorted_teams = League.sort_teams(self.teams, list(self.teams.keys()))
    
    place = 1
​
    while sorted_teams[-place] != team:
      #print(place)
      place += 1
    
    return place
​
def EPLResult(table, team):
​
  league = League(table)
​
  poss = league.find_team_place(team)
  exceptions = {1: '1st', 2: '2nd', 3: '3rd'}
​
  if poss in exceptions.keys():
    pos = exceptions[poss]
  else:
    pos = '{}th'.format(poss)
​
  Team = league.teams[team]
​
  return "{} came {} with {} points and a goal difference of {}!".format(Team.name, pos, Team.points, Team.gdif)

