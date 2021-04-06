
def is_goal_scored(goal):
  for row in range(3):
    if "0" in goal[row][0]:
      ind1 = goal[row][0].index("#")
      ind2 = goal[row][0].index("0")
      ind3 = goal[row][0].index("#", ind1+1)
      if ind2 > ind1 and ind2 < ind3:
        return True
  return False

