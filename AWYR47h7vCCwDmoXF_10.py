
from re import * 
def is_goal_scored(goal):
  pattern = r"^\s+#\s*0\s+#\s+$"
  l = []
  for lst in goal:
    for string in lst:
      x = match(pattern, string)
      l.append(bool(x))
  y = sum(l)
  return(bool(y))

