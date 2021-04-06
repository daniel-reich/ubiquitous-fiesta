
def dice_game(scores):
  players = ['p1', 'p2', 'p3', 'p4']
  scores = scores[::-1]
  while len(players) > 1:
    turn = []
    for player in players:
      turn.append({'s':scores.pop(), 'p':player})
    turn.sort(key = lambda t:(sum(t['s']), t['s'][0]))
    last1, last2 = turn[:2]
    if last1['s'] != last2['s']:
      players.remove(last1['p'])
  return players[0]

