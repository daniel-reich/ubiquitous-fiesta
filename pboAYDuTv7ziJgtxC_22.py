
def min_turns(current, target):
  count = 0
  for i in range(4):
    v = int(current[i]) - int(target[i])
    v = abs(v)
    count += min(v,10-v)
  return count

