
def is_goal_scored(goal):
  return any([2<i[0].find('0')<8 for i in goal[:-4]])

