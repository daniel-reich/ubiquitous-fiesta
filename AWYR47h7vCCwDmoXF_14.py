
def is_goal_scored(goal):
  return '0' in ''.join([x[3:-3] for y in goal[:3] for x in y])

