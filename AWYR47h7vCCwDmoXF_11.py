
def is_goal_scored(goal):
  A=goal[0][0][3:8]
  B=goal[1][0][3:8]
  C=goal[2][0][3:8]
  return '0' in A+B+C

