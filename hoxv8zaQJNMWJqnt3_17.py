
def is_heteromecic(n, goal = None):
  if goal == None:
    goal = n
    return is_heteromecic(0, goal)
  elif n*(n+1) == goal:
    return True
  elif n*(n+1) > goal:
    return False
  else:
    return is_heteromecic(n+1, goal)

