
def pirates_killed(gold, tolerance):
  diff = [max(gold)-x for x in gold]
  return any([True if diff[i]>tolerance[i] else False for i in range(len(diff))])

