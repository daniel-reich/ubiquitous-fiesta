
def dice_game(scores):
# this is a hot mess but stfu I'm learning
  players = ["1", "2", "3", "4"]
  n = len(players)
  while n > 1:
    this_round = scores[:n]
    scores = scores[n:]
    totals = [sum(dice) for dice in this_round]
    lowest = min(totals)
    if totals.count(lowest) == 1:
      i = totals.index(lowest)
      players.pop(i)
      n -= 1
    else:
      indices = [i for i in range(n) if totals[i] == lowest]
      firsts = [this_round[i][0] for i in range(n) if totals[i] == lowest]
      lowest = min(firsts)
      if firsts.count(lowest) == 1:
        i = firsts.index(lowest)
        players.pop(indices[i])
        n -= 1
  return "p{}".format(players[0])

