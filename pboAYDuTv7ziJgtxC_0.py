
def min_turns(current, target):
  current = [int(n) for n in current]
  target = [int(n) for n in target]
  return sum(min(abs(a-b), 10-abs(a-b)) for a, b in zip(current,target))

