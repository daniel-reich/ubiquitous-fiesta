
def is_goal_scored(goal):
  for i in range(len(goal)):
    for j in range(len(goal[i][0])):
      if goal[i][0][j] == '0':
        return i < 3 and 2 < j < 8

