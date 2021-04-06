
def score(p):
  return p[0] + p[1]
def pair1(p):
  return p[0]
​
def dice_game(scores):
  players = ["p1","p2","p3","p4"]
  while len(players) > 1:
    players.sort()
    scores1 = scores[:len(players)]
    scores = scores[len(players)::]
    results = dict(zip(players,scores1[:len(players)]))
    players.sort(key = lambda x: (score(results[x]),pair1(results[x])))
    if score(results[players[0]]) != score(results[players[1]]):
      players.pop(0)
      current =- 1
    elif pair1(results[players[0]]) != pair1(results[players[1]]):
      players.pop(0)
      current =- 1
  return players[0]

