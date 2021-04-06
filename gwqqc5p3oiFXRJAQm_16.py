
def football_points(wins, draws, losses):
  win_p = wins * 3
  draw_p = draws * 1
  losses_p = losses * 0
  totalpoints = win_p + draw_p + losses_p
  return totalpoints

