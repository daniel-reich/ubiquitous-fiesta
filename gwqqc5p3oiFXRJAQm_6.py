
def football_points(wins, draws, losses):
  wins *= 3
  draws *= 1
  losses *= 0
  return wins + draws + losses
football_points(1, 2, 3)

