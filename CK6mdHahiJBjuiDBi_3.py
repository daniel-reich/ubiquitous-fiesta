
def can_fit(weights, bags):
  sum = 0
  for i in weights:
    sum+=i
  if (sum/bags)<=10:
    return True
  else:
    return False

