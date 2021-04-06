
def is_goal_scored(goal):
  for i in range(3):
    if '0' in goal[i][0][3:-3]: return True
  return False

