
def min_turns(current, target):
  result = 0
  current, target = list(str(current)), list(str(target))
  for c, t in zip(current, target):
    c, t = int(c), int(t)
    result += min(abs(c-t), 10-abs(c-t))
  return result

