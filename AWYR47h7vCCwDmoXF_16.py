
def is_goal_scored(goal):
  for i in goal:
    i = i[0].replace(" ", "")
    if "#0#" in i and not "###" in i: return True
  return False

