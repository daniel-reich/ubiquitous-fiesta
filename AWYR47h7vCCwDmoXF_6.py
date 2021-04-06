
def is_goal_scored(goal):
  for i in range(7):
    for j in range(10):
      if goal[i][0][j] == '0':
        return 3<=j<= 7 and 0<=i<=2
  return False

