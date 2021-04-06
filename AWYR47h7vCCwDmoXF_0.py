
def is_goal_scored(goal):
  return any('0' in x[0][3:8] for x in goal[:3])

