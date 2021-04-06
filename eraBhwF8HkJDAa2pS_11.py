
def pirates_killed(gold, tolerance):
  diff = [max(gold)-item for item in gold]
​
  for i in range(len(diff)):
    if diff[i] > tolerance[i]:
      return True
  return False

