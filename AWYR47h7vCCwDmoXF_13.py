
def is_goal_scored(goal):
  return "0" in "".join(goal[i][0][2:-2] for i in [0,1,2])

