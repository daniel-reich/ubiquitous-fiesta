
def harry(po):
  if not sum(map(sum, po)):
    return -1
​
  p1 = sum(list(zip(*po))[0]) + sum(po[-1][1:])
  p2 = sum(po[0]) + sum(list(zip(*po))[-1][1:])
​
  return max(p1, p2)

