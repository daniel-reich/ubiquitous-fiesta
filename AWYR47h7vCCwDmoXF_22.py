
def is_goal_scored(goal):
  return any([True  if "0" in "".join(i) and "#" in "".join(i).split("0")[0] and "#" in "".join(i).split("0")[-1] and goal.index(i) < 3 else False for i in goal])

