
def min_turns(current, target):
  c = [int(i) for i in list(current)]
  t = [int(i) for i in list(target)]
  return sum([min(abs(c[i] - t[i]), 10 - abs(c[i] - t[i])) for i in range(4)])

