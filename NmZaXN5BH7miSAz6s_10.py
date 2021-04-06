
def check_places(leaderboard):
  count = 1
  places = []
  for index in range(len(leaderboard)):
    if index != 0 : 
      if leaderboard[index] != leaderboard[index-1]:
        count += 1
    places.append(count)
  return places
​
def new_score(leaderboard,newscore):
  tmp = leaderboard
  tmp.append(newscore)
  tmp.sort()
  return tmp[::-1]
​
def climbing_leaderboard(ranked, player):
  record = []
  leaderboard = ranked
  for score in player:
    leaderboard = new_score(leaderboard,score)
    p = check_places(leaderboard)
    i = leaderboard.index(score)
    record.append(p[i])
  return record

