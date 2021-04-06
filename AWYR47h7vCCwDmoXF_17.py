
def is_goal_scored(goal):
  return True if str([i[0][3:8] for i in goal[:3]]).find('0')!=-1 else False

