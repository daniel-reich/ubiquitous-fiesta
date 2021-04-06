
def is_goal_scored(goal):
  return '0' in ''.join(str(row)[5:10] for row in goal[:3])

