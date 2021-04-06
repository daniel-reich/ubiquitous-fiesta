
def is_goal_scored(goal):
  goal = [goal[i][0][3:8] for i in range(3)]
  return any('0' in row for row in goal)

