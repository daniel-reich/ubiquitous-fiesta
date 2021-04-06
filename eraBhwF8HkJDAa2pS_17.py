
def pirates_killed(gold, tolerance):
  diff = [max(gold)-g for g in gold]
  i=0
  for t in tolerance:
    if t<diff[i]:
      return True
    i+=1
  return False

