
def football(score,lst=[]):
  if sum(lst)==score:
    return 1
  elif sum(lst)>score:
    return 0
  return sum([football(score,lst+[i]) for i in [2,3,6,7,8] if len(lst)==0 or i>=lst[-1]])

