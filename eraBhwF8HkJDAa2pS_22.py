
def pirates_killed(gold, tolerance):
  diff = [max(gold)-i for i in gold]
  for i in range(len(gold)):
    if tolerance[i] < diff[i]:
      return True
  return False

