
def schoty(frame):
  l = [len(e.split('---')[0]) for e in frame]
  total = 0
  ep = 6
  while ep >= 0:
    for e in l:
      total = total + e * (10**ep)
      ep -= 1
  return total

