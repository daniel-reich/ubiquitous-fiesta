
def pirates_killed(gold, tolerance):
  for i in range(len(gold)):
    if max(gold)-gold[i]>tolerance[i]: return True
  return False

