
def pirates_killed(gold, tolerance):
  diff=[-(i - max(gold)) for i in gold]
  return sum([1 for i in range(len(gold)) if tolerance[i]<diff[i]]) > 0

