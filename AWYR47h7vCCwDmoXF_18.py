
def is_goal_scored(goal):
  for i in range(3):
    if "0" in goal[i][0][3:8]: return True
  return False

