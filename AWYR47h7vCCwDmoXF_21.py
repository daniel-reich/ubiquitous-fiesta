
def is_goal_scored(goal):
  return '0' in str([l[0][3:10] for l in goal[:3]])

