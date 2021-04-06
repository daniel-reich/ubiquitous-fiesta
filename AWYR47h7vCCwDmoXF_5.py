
def is_goal_scored(goal):
  for i in range(0,3):
    string = "".join(goal[i])
    if string.count("0") > 0:
      idx = string.index("0")
      return True if idx > 2 and idx < 8 else False
  return False

