
def dice_game(scores):
  players = ['p1', 'p2', 'p3', 'p4']
  while len(players) > 1:
    round = sorted([(s[0] + s[1], s[0], players[i]) for i, s in enumerate(scores[:len(players)])])
    scores = scores[len(players):]
    if round[0][0] < round[1][0] or round[0][1] < round[1][1]:
      players.remove(round[0][2])
  return players[0]

