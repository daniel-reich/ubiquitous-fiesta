
import re
def is_goal_scored(goal):
  for row in goal:
    if "0" in row[0]:
      if row[0].count("#") != 2:
        return False
      else:
        return bool(re.search(r'#\s*0\s*#',row[0]))

